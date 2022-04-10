# Analysing the Condomium Market in Singapore 

This repo contains the code for our final project in [CS5228](https://nusmods.com/modules/CS5228/knowledge-discovery-and-data-mining) at the School of Computing, National University of Singapore. 

Our team is named Data Nerds and our members are Aiden Low, Raivat Shah and Reshma Jawale. 

## System Requirements

* `Python` v3.9 and above 
*  `Jupyter Notebook` (you might already have this if you have [anaconda](http://anaconda.com). Check this guide to install if you don't have it already)
* If you're planning to run this on a remote machine, try to optimise/pick machines with a better CPU as against memory (RAM) or GPU as our evidence suggests RAM and GPU aren't as crucial to this code as much as the CPU. We trained using a CPU-optimised Droplet from Digital Ocean. 

## Setup 

Clone the repo (replace the link if you prefer HTTPS links):

```
git clone git@github.com:aidenywl/data-mining-property-prices.git 
cd data-mining-property-prices
```

Setup a virtual environment and install the required libraries:

```
python -m venv env
source env/bin/activate 
pip install -r requirements.txt
```

## Project Stucture

All the code is under the `src` folder. We have two types of code in this project, `library` and `notebooks`. 

`Notebooks`:

We organize our notebooks around the tasks we complete in our report. Notebooks are in `/src/`. 

* `approach1.ipnyb`: contains the code for approach 1
* `approach2a.ipnyb`: contains the code for approach 2A
* `approach2b.ipnyb`: contains the code for approach 2B
* `approach3a.ipnyb`: contains the code for approach 3a
* `eda.ipnyb`: contains the code for our exploratory data anlysis and for generating the charts used in our report

`Library Code`:

We abstract out common functions used in all the notebooks under a `library` package under `/src/`. Individual files are at `/src/library_code`. 

* `auxiliary.py` contains code for processing the auxiliary data
* `cleaning.py` contains code for cleaning the primary dataset
* `constants.py` contains the constant to store column names we ignore 
* `imputation.py` contains the code for imputation of values

`Data`: 

All the data is found in `/data/`.

* `test.csv` and `train.csv` are part of the primary dataset and are respectively the test and training sets. 
* `/data/additional_data` contains the data for consumer price index.
* `/data/auxiliary-data` contains the data for distances to prominent places in Singapore

