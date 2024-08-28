# Representative Arm Identification

This repository contains the code implementation for the **Representative Arm Identification** problem, as described in the paper ["Representative Arm Identification: A Fixed Confidence Approach to Identify Cluster Representatives"](https://arxiv.org/pdf/2408.14195). The approach focuses on identifying representative arms from clusters within a dataset, providing a fixed confidence solution to this problem.

## Overview

![Representative Arm Identification](path/to/your/image.png)

The repository provides scripts to apply the Representative Arm Identification algorithm on both the **Movielens dataset** and artificial datasets. Additionally, it includes a script for calculating the Delta (Δ) value as defined in the paper.
## Usage Instructions

### Movielens Dataset

To apply the algorithm to the Movielens dataset, follow these steps:

1. **Download the Dataset:**
   - Download the `rating.csv` file from the [Movielens 20M Dataset on Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset?select=rating.csv).

2. **Configure the Script:**
   - Open the file `ml_main.py`.
   - Set the variable `dataset_path` to the path of the `rating.csv` file you downloaded.
   - Define the cluster and required arrays as specified in the paper.

3. **Run the Script:**
   - Execute `ml_main.py` to start the algorithm.

### Artificial Dataset

For experiments using artificial datasets:

1. **Configure the Script:**
   - Open the file `main.py`.
   - Set the variable `Arms` with a list of true mean values.
   - Specify the `required` arms from each cluster and the `cluster` with the number of arms in each cluster.
   - Set the `merging` variable to `True` if you want to run the merging variation of the algorithm, otherwise set it to `False`.

2. **Run the Script:**
   - Execute `main.py` to run the algorithm on the artificial dataset.

### Calculating Delta (Δ)

To calculate the Delta (Δ) value as per the algorithm:

1. **Configure the Script:**
   - Open the file `delta_calculator.py`.
   - Set the `Arms` variable with a list of true mean values.
   - Specify the `required` arms and the `cluster` with the number of arms in each cluster.

2. **Run the Script:**
   - Execute `delta_calculator.py` to compute the Delta (Δ) value.

## Citation

If you use this code or refer to the methodology in your work, please cite the following paper:

```bibtex
@misc{gharat2024representativearmidentificationfixed,
      title={Representative Arm Identification: A Fixed Confidence Approach to Identify Cluster Representatives}, 
      author={Sarvesh Gharat and Aniket Yadav and Nikhil Karamchandani and Jayakrishnan Nair},
      year={2024},
      eprint={2408.14195},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2408.14195}, 
}
