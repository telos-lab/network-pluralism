# Network Pluralism

This is the replication package accompanying the following paper:

> Titus Pünder and Corinna Coupette. *The Power of Network Pluralism: Multi-Perspective Modeling of Heterogeneous Legal Document Networks* 
> DOI: [10.48550/arXiv.2512.05679](https://doi.org/10.48550/arXiv.2512.05679)

## Setup: Data

There are two ways two run this reproducability package.
- Including `downloading the raw data` and `preprocessing`: This will download the raw data from the original sources. As these provide the data up to date, the results might not correspond with the results presented in the paper.
- Only `generating results and figures`: Download the preprocessed data as of the paper's latest download date from this [Donwload Link]() and place it into the `data`-folder as specific below.

In any case, all data should be stored in a `data`-folder. You can specifiy it's location by providing a `DATA_PATH` variable in your `.env` file. By default, a folder will be created at the location of this repository.

## Setup: Environment

We recommend installing the Python requirements into a virtual environment, e.g. using `uv` ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))

```bash
uv sync
```

Now, you should be able to run all our code.


## Structure

- `notebooks`: Code for data analysis and plotting 
    - `general`:
        - `depth.ipynb`: Describing *avaliable* depth in statutes and *exploited* depth within the observed references.
        - `base_network_description.ipynb`: Describing the size of the *base network* and its composition.
        - `dynamic_counting.ipynb`: Explore several ways on how (not) to resolve the legislative side in reference networks and analyze their impacts on a standard metric (centrality).
    - `case_study_1`: Results and figures of the first case study:
        - `source_and_target.ipynb`: Computing source and target distributions of the top 10 referenced sections.
        - `ranks.ipynb`: Plotting how ranks relate to a modeling and parameter choices.
    - `case_study_2`: Results and figures of the first case study:
        - `reference_distributions.ipynb`: Showing and comparing the distributions of outgoing and incoming references across two levels of granularity.
        - `general_norms.ipynb`: Showing the overpresentations of nodes at a coarse grained network model.
        - `decision_vs_paragraph.ipynb`: Plotting co-reference frequency at two different resolution levels.
        - `source_granularity.ipynb`: Strongest neighbors observed for an example section at different granularity levels.
        - `strength_threshold.ipynb`: Introducing thresholds and plotting their impact on ranks of strongest neighbors.
        - `reciprocity.ipynb`: Introducing reciprocity of pairwise relations and plotting bi-dimensional distributions (of in- and outgoin strength).
        - `areas_of_law.ipynb`: Example of strongest neighbors observed in filtered subsets.
- `figures_and_results`: Figures and results presented in the paper.
- `scripts`: Scripts resembling the pipeline.
- `src/network_pluralism`: The package underlying all other parts
    - `./access`: Acessing the network data.
    - `./download`: Downloading the orginal data.
    - `./preprocessing`: Pre-Processing the raw data (optional and yet to do).
