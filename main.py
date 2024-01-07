student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key[0])
    # print(value[0])
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(nato)
dic_one = {row['letter']: row['code'] for (index, row) in df.iterrows()}


# print(dic_one)
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    input_one = input("enter your name-").upper()
    try:
        output = [dic_one[l] for l in input_one]
    except KeyError:
        print("sorry only enter letters ")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
