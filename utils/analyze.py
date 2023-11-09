import pandas as pd
import matplotlib.pyplot as plt

def graph():
  df = pd.read_csv('prices.csv')
  print (df.head())