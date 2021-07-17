import csv
import random


def challenge_builder_simples_tenses_verb():
    simple_tenses = ['Preset', 'Past', 'Future']
    type = ['Phrase', 'Question']
    pronouns = ['I', 'You', 'He', 'She', 'It', 'We', 'They']

    with open('100_verbs.csv') as file_csv:
        verbs = [line for line in csv.reader(file_csv) if not line[1] == 'x']

    verb = random.choice(verbs)

    print(
        f"With the pronoun \033[33m{random.choice(pronouns)}\033[38m, "
        f"create a \033[33m{random.choice(type)} \033[38m"
        f"in the \033[33m{random.choice(simple_tenses)} \033[38m"
        f"tense with the verb to \033[33m{verb[0]} | {verb[1]}\033[38m (Affirmative and Negative)"
    )


[challenge_builder_simples_tenses_verb() for item in range(10)]
