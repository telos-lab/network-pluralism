# Network Pluralism Replication Package (Data and Code)

This is the replication package accompanying the following paper:

> Titus Pünder and Corinna Coupette. *The Power of Network Pluralism: Multi-Perspective Modeling of Heterogeneous Legal Document Networks*, Published in *The European Physical Journal B*, 2026
> DOI: [10.1140/epjb/s10051-026-01178-3](https://doi.org/10.1140/epjb/s10051-026-01178-3)

## Setup: Data

If you have **downloaded this repo as a reproducibility package from Zenodo**, the required data is already placed in the folder `network_pluralism_data`.

If you **have cloned this repo from GitHub**, you have to download the accompanying dataset as specified in the following paragraph.

Download the *preprocessed* data as of the paper's latest download date from this [Data Repository](https://doi.org/10.5281/zenodo.17780510) and place it in the `data`-folder. You can specify its location by providing a `DATA_PATH` variable in your `.env` file. By default, a folder will be created at the root of this repository.

## Setup: Environment

We recommend installing the Python requirements into a virtual environment, e.g., using `uv` ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))

```bash
uv sync
```

Now, you should be able to run all our code.

## Running the code

This reproducibility package builds on a set of Jupyter notebooks. You can either:

1. Open *individual* notebooks, examine them, and execute cells in the way you're used to.
2. Run *all* notebooks using the command below. Note: this will overwrite the notebooks to populate cell outputs.

```bash
bash run_all_notebooks.sh
```

All figures and tables produced by the notebooks will be stored in the folder `figures_and_results`.

## Repository Structure

This repository is structured as follows:

- `notebooks`: Code for data analysis and plotting.
  - `general`:
        - `depth.ipynb`: Describing *available* depth in statutes and *exploited* depth within the observed references.
        - `base_network_description.ipynb`: Describing the size of the *base network* and its composition.
        - `dynamic_counting.ipynb`: Exploring several ways how (not) to resolve the legislative side in reference networks and analyze their impacts on a standard metric (centrality).
  - `case_study_1`: Results and figures of the first case study:
        - `source_and_target.ipynb`: Computing source and target distributions of the top 10 referenced sections.
        - `ranks.ipynb`: Plotting how ranks relate to modeling and parameter choices.
  - `case_study_2`: Results and figures of the second case study:
        - `reference_distributions.ipynb`: Showing and comparing the distributions of outgoing and incoming references across two levels of granularity.
        - `general_norms.ipynb`: Showing the overrepresentation of nodes in a coarse-grained network model.
        - `decision_vs_paragraph.ipynb`: Plotting co-reference frequency at two different resolution levels.
        - `source_granularity.ipynb`: Strongest neighbors observed for an example section at different levels of granularity.
        - `strength_threshold.ipynb`: Introducing thresholds and plotting their impact on ranks of strongest neighbors.
        - `reciprocity.ipynb`: Introducing reciprocity of pairwise relations and plotting bi-dimensional distributions (of incoming and outgoing strength).
        - `areas_of_law.ipynb`: Example of strongest neighbors observed in filtered subsets.
- `figures_and_results`: Figures and results presented in the paper.
- `scripts`: Scripts resembling the pipeline.
- `src/network_pluralism`: The package underlying all other parts, mainly access to the network data + some helper functions.

## Figures and Tables

All data-related figures and tables in the paper can be reproduced using the notebooks contained in this repository. Consult the table below for specific presentations:

| File   |      Figures      |  Tables |
|----------|:-------------:|------:|
| `depth.ipynb` | 3 |  |
| `base_network_description.ipynb` |   |  1 |
| `dynamic_counting.ipynb` |  | 4, 5 |
| `source_and_target.ipynb` | 6 | |
| `ranks.ipynb` | 7 |  |
| `reference_distributions.ipynb` | 8 |  |
| `general_norms.ipynb` |   | 2 |
| `decision_vs_paragraph.ipynb` |  9 |  |
| `source_granularity.ipynb` | 10 |  |
| `strength_threshold.ipynb` | 11 |  |
| `reciprocity.ipynb` | 12 b) |  |
| `areas_of_law.ipynb` | 13  |  |

## License

**Code**: BSD 3-Clause License, (c) 2025, telos-lab - See: `LICENSE`.
**Data**: CC BY-NC 4.0 - See: `DATALICENSE`.

