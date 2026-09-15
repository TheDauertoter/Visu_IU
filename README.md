# DLBDSEDAV01 – Explorative Data Analysis and Visualization

This repository contains the files used for the project report of the course **DLBDSEDAV01 – Explorative Data Analysis and Visualization**.

## Contents

* `usa_housing_kaggle.csv` – USA Housing dataset from [Kaggle](https://www.kaggle.com/datasets/afifahnajla/usa-housing-kaggle)
* `data_quality.py` – Data quality check for the kaggle dataset
* `binsizes.py` – Histogram of `Price` with different bin sizes
* `histogramm.py` – Histogram of `Price` with mean, median and standard deviation
* `perc_par.py` – Percentage distribution of `Price` relative to mean ± standard deviation
* `boxplott.py` – Box plot of `Price`
* `violin.py` – Violin plot of `Price`
* `corr.py` – Correlation heatmap of numerical variables (excluding `ZipCode`)

## Setup

Pull the repository and install the required packages:

```bash
pip install -r req.txt
```

The Python files can then be run individually to reproduce the visualizations.
