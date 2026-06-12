# importing libraries
import numpy as np
import panas as pd
import matplotlip.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import standardscaler
from sklearn import svm
from sklearn.metrics import accuracy_score

#loading the dataset
diabetes_dataset= pd.read_csv("datasets/diabetes.csv")
