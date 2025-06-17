# Efficient And Scalable Search For Statistics

This repository provides supplementary material for the research article *Efficient And Scalable Search For Statistics*. 

## Code

TBD

## Datasets

The two datasets ![D_l](https://latex.codecogs.com/svg.image?\mathcal{D}_{\ell}) and ![D_f](https://latex.codecogs.com/svg.image?\mathcal{D}_{f}) can be downloaded from [this Zenodo dataset](https://doi.org/10.5281/zenodo.15681384).

## Evaluation Questions

We provide the two sets of evaluation questions we present in the paper, as CSV files:
- [S_i.csv](S_i.csv) corresponds to the question set ![S_i](https://latex.codecogs.com/svg.image?\mathcal{S}_{i})
- [S_r.csv](S_r.csv) corresponds to the question set ![S_r](https://latex.codecogs.com/svg.image?\mathcal{S}_{r})

Each file has three columns: on for the ID of the question (`question_id`), one for the textual question (`question`), and one for the associated table ID (`table_id`).

## Systems Outputs

We provide all top-N table IDs that each model returned for both datasets and questions sets (except for Solo and Birdie on ![D_l](https://latex.codecogs.com/svg.image?\mathcal{D}_{\ell})) in the directory [systems_outputs](systems_outputs), under which are one sub-directory per system:
- [Birdie](systems_outputs/birdie), with outputs for ![D_lS_i](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{\ell}, \mathcal{S}_{i}\right)) ([birdie-D_l-S_i.csv](systems_outputs/birdie/birdie-D_l-S_i.csv)) and for ![D_lS_r](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{\ell}, \mathcal{S}_{r}\right)) ([birdie-D_l-S_r.csv](systems_outputs/birdie/birdie-D_l-S_r.scv)).
- [BM25](systems_outputs/bm25), with outputs for ![D_lS_i](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{\ell}, \mathcal{S}_{i}\right)) ([birdie-D_l-S_i.csv](systems_outputs/birdie/birdie-D_l-S_i.csv)), ![D_lS_r](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{\ell}, \mathcal{S}_{r}\right)) ([birdie-D_l-S_r.csv](systems_outputs/birdie/birdie-D_l-S_r.scv)), ![D_fS_i](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{f}, \mathcal{S}_{i}\right)), and ![D_fS_r](https://latex.codecogs.com/svg.image?\left(\mathcal{D}_{f}, \mathcal{S}_{r}\right)).



