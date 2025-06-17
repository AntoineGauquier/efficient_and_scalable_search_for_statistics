# Efficient And Scalable Search For Statistics

This repository provides supplementary material for the research article *Efficient And Scalable Search For Statistics*. 

## Code

TBD

## Datasets

The two datasets (the one with 2000 lightest tables and the full dataset) can be downloaded from [this Zenodo dataset](https://doi.org/10.5281/zenodo.15681384).

## Evaluation Questions

We provide the two sets of evaluation questions we present in the paper, as CSV files:
- [S_i.csv](S_i.csv) corresponds to the initial question set.
- [S_r.csv](S_r.csv) corresponds to the reformulated question set.

Each file has three columns: on for the ID of the question (`question_id`), one for the textual question (`question`), and one for the associated table ID (`table_id`).

## Systems Outputs

We provide the top-N table IDs returned by each system (excluding Solo and Birdie, which could not be indexed on the full dataset) for both datasets and both question sets. These outputs are located in the [systems_outputs](systems_outputs) directory, which contains a subdirectory for each system.

| System          | (Small Dataset, Initial Q. Set)                                | (Small Dataset, Reformulated Q. Set)                              | (Full Dataset, Initial Q. Set)                                  | (Full Dataset, Reformulated Q. Set)                              |
|-----------------|-----------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| Birdie          | [birdie-D_l-S_i.csv](systems_outputs/birdie/birdie-D_l-S_i.csv) | [birdie-D_l-S_r.csv](systems_outputs/birdie/birdie-D_l-S_r.csv)  | N/A                                                             | N/A                                                             |
| BM25            | [bm25-D_l-S_i.csv](systems_outputs/bm25/bm25-D_l-S_i.csv)       | [bm25-D_l-S_r.csv](systems_outputs/bm25/bm25-D_l-S_r.csv)        | [bm25-D_f-S_i.csv](systems_outputs/bm25/bm25-D_f-S_i.csv)       | [bm25-D_f-S_r.csv](systems_outputs/bm25/bm25-D_f-S_r.csv)       |
| Pneuma          | [pneuma-D_l-S_i.csv](systems_outputs/pneuma/pneuma-D_l-S_i.csv) | [pneuma-D_l-S_r.csv](systems_outputs/pneuma/pneuma-D_l-S_r.csv)  | [pneuma-D_f-S_i.csv](systems_outputs/pneuma/pneuma-D_f-S_i.csv) | [pneuma-D_f-S_r.csv](systems_outputs/pneuma/pneuma-D_f-S_r.csv) |
| Solo            | [solo-D_l-S_i.csv](systems_outputs/solo/solo-D_l-S_i.csv)       | [solo-D_l-S_r.csv](systems_outputs/solo/solo-D_l-S_r.csv)        | N/A                                                             | N/A                                                             |
| STAR with PEARL | [star_pearl-D_l-S_i.csv](systems_outputs/star_pearl/star_pearl-D_l-S_i.csv) | [star_pearl-D_l-S_r.csv](systems_outputs/star_pearl/star_pearl-D_l-S_r.csv) | [star_pearl-D_f-S_i.csv](systems_outputs/star_pearl/star_pearl-D_f-S_i.csv) | [star_pearl-D_f-S_r.csv](systems_outputs/star_pearl/star_pearl-D_f-S_r.csv) |
| STAR with SBERT | [star_sbert-D_l-S_i.csv](systems_outputs/star_sbert/star_sbert-D_l-S_i.csv) | [star_sbert-D_l-S_r.csv](systems_outputs/star_sbert/star_sbert-D_l-S_r.csv) | [star_sbert-D_f-S_i.csv](systems_outputs/star_sbert/star_sbert-D_f-S_i.csv) | [star_sbert-D_f-S_r.csv](systems_outputs/star_sbert/star_sbert-D_f-S_r.csv) |

Each of these CSV files has one column for the question ID (`question_id`), and 10 columns for the top-10 ranked tables (`table_id_rank_1`, `table_id_rank_2`, etc. up to `table_id_rank_10`). When some systems do not provide 10 tables, we let missing cells blank. 

## Annotations

We provide the manually annotated (question, table) pairs used to compute Relevance@k scores ([annotations.csv](annotations.csv)). We purposely included duplicates so that inter-annotator agreement can be verified. This CSV file contains one column for question ID (`question_id`), one for table ID (`table_id`), and one for the label (`label`): either *highly relevant*, *relevant* or *not_relevant*.

## Metrics Re-Generation

We provide two scripts to re-compute both metrics:
- [compute_HitRate_scores.py](compute_HitRate_scores.py) computes the HitRate@k metric for k from 1 to 10. It can be used in CLI by running `python3 compute_HitRate_scores.py <question_set_path> <system_output_path>`, where `question_set_path` is either [S_i.csv](S_i.csv) or [S_r.csv](S_r.csv), and `system_output_path` is the file containing the search outputs to be evaluated (for instance [star_sbert-D_l-S_r.csv](systems_outputs/star_sbert/star_sbert-D_l-S_r.csv)).
- [compute_Relevance_scores.py](compute_Relevance_scores.py) computes the Relevance@k metric for k from 1 to 5. It can be used in CLI by running `python3 compute_Relevance_scores.py <annotations_path> <system_output_path>`, where `annotations_path` is basically [annotations.csv](annotations.csv), and `system_output_path` exactly as for [compute_HitRate_scores.py](compute_HitRate_scores.py).