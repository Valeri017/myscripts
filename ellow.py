import pandas as pd
from sklearn.datasets import load_breast_cancer
columns = ['mean radius', 'mean texture', 'mean perimetr', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension', 'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error','concavity error','concave points error', 'symmetry error', 'fractal dimension error', 'worst radius','worst texture', 'worst perimeter', 'worst area','worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
dataset = load_breast_cancer()
data = pd.DataFrame(dataset['data'], columns=columns)
data['cancer'] = dataset['target']
display(data.head())
display(data.info())
display(data.isna().sum())
display(data.describe())
