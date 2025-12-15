# Network Pluralism

This is the replication package accompanying the following paper:

> Titus Pünder and Corinna Coupette. *The Power of Network Pluralism: Multi-Perspective Modeling of Heterogeneous Legal Document Networks* 
> DOI: [10.48550/arXiv.2512.05679](https://doi.org/10.48550/arXiv.2512.05679)

# Setup: Data

There are two ways two run this reproducability package.
- Including `downloading the raw data` and `preprocessing`: This will download the raw data from the original sources. As these provide the data up to date, the results might not correspond with the results presented in the paper.
- Only `generating results and figures`: Download the preprocessed data as of the paper's latest download date from this [Donwload Link](https://drive.google.com/file/d/1h8oroadqqXJCLJqnLdEnYOMguHa7cfZ0/view) and place it into the `data`-folder as specific below.

In any case, all data should be stored in a `data`-folder. You can specifiy it's location by providing a `DATA_PATH` variable in your `.env` file. By default, a folder will be created at the location of this repository.

## Setup: Environment

We recommend installing the Python requirements into a virtual environment, e.g. using `uv` ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))

```bash
uv sync
```

Now, you should be able to run all our code.


# Structure

- `notebooks`: Data analysis and plotting code
- `figures`: Figures used in our paper
- `scripts`: Scripts resembling the pipeline.
- `src/network_pluralism`: The package underlying all other parts
    - `./access`: Acessing the graph data.
    - `./download`: Downloading the orginal data.
    - `./preprocessing`: Pre-Processing the raw data.
