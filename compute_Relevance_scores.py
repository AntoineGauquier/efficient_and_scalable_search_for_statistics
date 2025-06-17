import csv, os, sys

def compute_Relevance_scores(annotations_path, system_output_path):
	label_scores = {
		'highly_relevant': 2,
		'relevant': 1,
		'not_relevant': 0
	}

	raw_scores = {}
	with open(annotations_path, 'r', newline='') as f_r:
		reader = csv.DictReader(f_r)
		for row in reader:
			qid = row['question_id']
			table_id = row['table_id'].strip()
			score = label_scores[row['label']]

			key = (qid, table_id)
			if key not in raw_scores:
				raw_scores[key] = []
			raw_scores[key].append(score)

	resolved_scores = {}
	for key in raw_scores:
		resolved_scores[key] = max(raw_scores[key])

	rankings = {}
	with open(system_output_path, 'r', newline='') as f_r:
		reader = csv.DictReader(f_r)
		for row in reader:
			qid = row['question_id']
			ranked_tables = []

			for i in range(1, 6):
				tid = row.get(f'table_id_rank_{i}', '').strip()
				if tid:
					ranked_tables.append(tid)

			rankings[qid] = ranked_tables

	k_values = [1, 2, 3, 4, 5]
	scores_by_k = {k: [] for k in k_values}

	for qid in rankings:
		ranked_tables = rankings[qid]

		for k in k_values:
			top_k = ranked_tables[:k]
			score = 0
			for table_id in top_k:
				score += resolved_scores[(qid, table_id)]
			scores_by_k[k].append(score)

	return [round(sum(scores_by_k[k]) / len(scores_by_k[k]), 2) for k in k_values]

def main():
	if len(sys.argv) != 3:
		print(f"Usage: python3 {sys.argv[0]} <annotations_path> <system_output_path>")
	else:
		annotations_path = sys.argv[1]
		system_output_path = sys.argv[2]

		scores = compute_Relevance_scores(annotations_path, system_output_path)
		
		for k, score in enumerate(scores, 1):
			print(f"Relevance@{k}: {score}")

if __name__ == '__main__':
	main()