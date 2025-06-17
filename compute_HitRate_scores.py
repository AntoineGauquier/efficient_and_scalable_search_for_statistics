import csv, os, sys

def compute_HitRate_scores(question_set_path, system_output_path):
    ground_truths = {}

    with open(question_set_path, 'r', newline='') as f_r:
        reader = csv.DictReader(f_r)
        for row in reader:
            qid = int(row['question_id'])
            table_id = row['table_id']
            ground_truths[qid] = table_id

    outputs = {}
    with open(system_output_path, 'r', newline='') as f_r:
        reader = csv.DictReader(f_r)
        for row in reader:
            qid = int(row['question_id'])
            table_ids = [row[f'table_id_rank_{i}'] for i in range(1, 11) if row.get(f'table_id_rank_{i}', '').strip()]
            outputs[qid] = table_ids

    hits_at_k = [0] * 10
    total = 0

    for qid, correct_table in ground_truths.items():
        table_ids_list = outputs[qid]
        for k in range(1, 11):
            if correct_table in table_ids_list[:k]:
                hits_at_k[k - 1] += 1
        total += 1

    return [round(number_hits / total, 2) for number_hits in hits_at_k]

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <question_set_path> <system_output_path>")
    else:
        question_set_path = sys.argv[1]
        system_output_path = sys.argv[2]

        scores = compute_HitRate_scores(question_set_path, system_output_path)
        
        for k, score in enumerate(scores, 1):
            print(f"HitRate@{k}: {score}")

if __name__ == '__main__':
    main()
