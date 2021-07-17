import csv
import random

simple_tenses = ['Preset', 'Past', 'Future']

tipe = ['Phrase', 'Question']

with open('100_verbs.csv') as file_csv:
    verbs = [line for line in csv.reader(file_csv)]

verb = random.choice(verbs)

print(f"Generate a {random.choice(tipe)} "
      f"in the {random.choice(simple_tenses)} "
      f"tense with the verb to {verb[0]} | {verb[1]}")
