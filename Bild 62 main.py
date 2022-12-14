# Packages *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

# Filepath of CSV file *
disease_data = "Disease Data.csv" # Edit this line to change the filepath

# Functions *
def load_data(disease_data): 
	'''This function loads in the data into a pandas dataframe, and converts columns names to lowercase'''
	disease_df = pd.read_csv(disease_data)
	disease_df.columns = [i.lower() for i in disease_df.columns]
	return disease_df

def get_table(disease_df, disease_name):
	'''Returns sub-dataframe of year plus specified disease'''
	disease_name = disease_name.lower()
	return disease_df[['year', disease_name]]

def get_graph(disease_df, disease_name):
  '''Generates a line plot of number of cases for specified disease'''
  sub_disease_df = get_table(disease_df, disease_name)
  fig, ax = plt.subplots()
  plt.plot(sub_disease_df['year'], sub_disease_df[disease_name])
  disease_name_capitalized = disease_name.capitalize()

  # Plot formatting
  ax.set_title(disease_name_capitalized)
  ax.set_xlabel('Year')
  ax.set_ylabel('Number of Cases')
  plt.show()

# Load Data *
disease_df = load_data(disease_data)

# Create a graph for each unique disease in dataset *
unique_disease_names = [i for i in disease_df if i != 'year']
for disease_name in unique_disease_names:
  get_graph(disease_df, disease_name)

# example get_graph(disease_df, 'measles')

# the rest of the code revolves around the question game
diseases = ["measles", "diphtheria", "mumps", "pertussis"]
game_df = rd.sample(diseases,2)
def check(disease, game_df):
    if disease in game_df:
        get_graph(disease_df,(disease))
    else:
        print()
check('diphtheria',game_df)
check('measles',game_df)
check('mumps',game_df)
check('pertussis',game_df)
print("which disease was more prevalent during the year 2015?")

measles = 214808
diphtheria = 4535
mumps = 385781
pertussis = 156065
def check_cases(correct_disease,disease_list):
    if all(correct_disease >= x for x in disease_list):
        print("correct!")
    else:
        print("wrong!")
# example: check_cases(mumps,(measles, mumps))
# lines 45-67 would be run as a complete cell, upon asking to start the game.
# you then answer the question at the end with the code: check_cases(correct_disease,disease_list)
# the first disease is the one you think is the most prevalent, after that you put the list of diseases you are choosing from.
