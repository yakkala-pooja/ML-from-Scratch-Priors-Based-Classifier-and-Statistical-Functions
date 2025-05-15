# Prior Probability Classifier with Custom Statistical Functions

This repository presents a lightweight machine learning project built from scratch in Python. It includes the implementation of custom statistical functions and a simple prior-based probabilistic classifier. The project demonstrates how to model classification problems using only prior class distributions, providing a baseline understanding of class imbalance and prediction strategies.

## Project Structure

```
.
├── util.py              # Custom statistical functions: mean, stdev, sampleMean, covariance
├── classifiers.py       # Prior probability-based classifier
├── test_notebook.ipynb  # Data simulation, testing, and visualization
└── README.md            # Project documentation
```

## Features

### `util.py` – Custom Statistical Functions

Manually implemented versions of commonly used statistical measures without relying on NumPy’s statistical methods.

- `mean(data)`: Computes the arithmetic mean.
- `stdev(data)`: Computes the sample standard deviation.
- `sampleMean(data)`: Calculates the mean for each feature column.
- `covariance(x, y)`: Computes the covariance between two lists.

These functions were validated by comparing outputs with equivalent NumPy functions using synthetic data generated with `numpy.random.normal`.

### `classifiers.py` – `Priors` Class

A basic probabilistic classifier that uses only prior class distributions:

- Estimates `P(ωj)` from labeled data.
- Predicts the class with the highest prior (most frequent class).
- Designed to support **multiple classes**.
- Contains a `retrain()` method for reusing the classifier with new data.

## Testing & Evaluation

### Data Simulation

- A synthetic dataset with **1,000 samples** and two classes:
  - **"Stress"** (430 samples), heart rate ~110
  - **"Not Stress"** (570 samples), heart rate ~65
- Dataset includes:
  - One feature: `"Heart-Rate"`
  - One label: `"Class"`

Pandas `groupby()` and `describe()` were used to verify class balance and feature distributions.

### Classifier Testing

- Evaluated the classifier on heart rate inputs from **40 to 140**.
- Visualized predictions using Matplotlib.
- Because the model uses prior probabilities only, it always predicts the **most common class**.

## Requirements

Install required dependencies:

```bash
pip install numpy pandas matplotlib
```

## How to Run

1. Clone the repository.
2. Open `test_notebook.ipynb` using Jupyter Notebook or JupyterLab.
3. Run each cell to:
   - Compare custom statistical functions against NumPy.
   - Generate and inspect the dataset.
   - Train and test the Prior classifier.
   - Plot the classifier's predictions over a heart-rate range.

## Learning Objectives

- Implement statistical computations from scratch.
- Understand how prior class distributions can drive classification.
- Explore effects of class imbalance.
- Practice data generation, validation, and visualization workflows.

## Future Work

- Add support for likelihoods to build a full Naive Bayes classifier.
- Extend to multi-feature input using conditional independence assumptions.
- Integrate accuracy and confusion matrix evaluations for deeper insights.
