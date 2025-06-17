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

## System Outputs

We provide the top-N table IDs returned by each system (excluding Solo and Birdie, which could not be indexed on the full dataset) for both datasets and both question sets. These outputs are located in the [systems_outputs](systems_outputs) directory, which contains a subdirectory for each system.

| System          | (Small Dataset, Initial Q. Set) Questions                                | (Small Dataset, Reformulated Q. Set) Questions                              | (Full Dataset, Initial Q. Set)                                  | (Full Dataset, Reformulated Q. Set)                              |
|-----------------|-----------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| Birdie          | [birdie-D_l-S_i.csv](systems_outputs/birdie/birdie-D_l-S_i.csv) | [birdie-D_l-S_r.csv](systems_outputs/birdie/birdie-D_l-S_r.csv)  | N/A                                                             | N/A                                                             |
| BM25            | [bm25-D_l-S_i.csv](systems_outputs/bm25/bm25-D_l-S_i.csv)       | [bm25-D_l-S_r.csv](systems_outputs/bm25/bm25-D_l-S_r.csv)        | [bm25-D_f-S_i.csv](systems_outputs/bm25/bm25-D_f-S_i.csv)       | [bm25-D_f-S_r.csv](systems_outputs/bm25/bm25-D_f-S_r.csv)       |
| Pneuma          | [pneuma-D_l-S_i.csv](systems_outputs/pneuma/pneuma-D_l-S_i.csv) | [pneuma-D_l-S_r.csv](systems_outputs/pneuma/pneuma-D_l-S_r.csv)  | [pneuma-D_f-S_i.csv](systems_outputs/pneuma/pneuma-D_f-S_i.csv) | [pneuma-D_f-S_r.csv](systems_outputs/pneuma/pneuma-D_f-S_r.csv) |
| Solo            | [solo-D_l-S_i.csv](systems_outputs/solo/solo-D_l-S_i.csv)       | [solo-D_l-S_r.csv](systems_outputs/solo/solo-D_l-S_r.csv)        | N/A                                                             | N/A                                                             |
| STAR with PEARL | [star_pearl-D_l-S_i.csv](systems_outputs/star_pearl/star_pearl-D_l-S_i.csv) | [star_pearl-D_l-S_r.csv](systems_outputs/star_pearl/star_pearl-D_l-S_r.csv) | [star_pearl-D_f-S_i.csv](systems_outputs/star_pearl/star_pearl-D_f-S_i.csv) | [star_pearl-D_f-S_r.csv](systems_outputs/star_pearl/star_pearl-D_f-S_r.csv) |
| STAR with SBERT | [star_sbert-D_l-S_i.csv](systems_outputs/star_sbert/star_sbert-D_l-S_i.csv) | [star_sbert-D_l-S_r.csv](systems_outputs/star_sbert/star_sbert-D_l-S_r.csv) | [star_sbert-D_f-S_i.csv](systems_outputs/star_sbert/star_sbert-D_f-S_i.csv) | [star_sbert-D_f-S_r.csv](systems_outputs/star_sbert/star_sbert-D_f-S_r.csv) |

