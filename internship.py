#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

# Define a function to generate multiple-choice questions with shuffled options
def generate_multiple_choice_question(rule, num_questions):
    questions = []
    for _ in range(num_questions):
        if rule == "list_to_matrix_shape":
            n = random.randint(1, 5)
            m = random.randint(1, 5)
            question = f"If you convert a Python list with {n * m} elements into a matrix, what will be the shape of the resulting matrix?"
            choices = [
                f"({n}, {m})",
                f"({m}, {n})",
                f"(1, {n})",
                f"({n}, 1)"
            ]
            answer = f"({n}, {m})"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_access":
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            question = f"How would you access an element at row {row} and column {col} in the corresponding matrix?"
            choices = [
                f"matrix[{row}][{col}]",
                f"matrix({row}, {col})",
                f"matrix[{col}][{row}]",
                f"matrix({col}, {row})"
            ]
            answer = f"matrix[{row}][{col}]"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_conversion":
            question = "What Python library can be used to convert a list into a matrix (2D array)?"
            choices = [
                "NumPy",
                "pandas",
                "matplotlib",
                "scikit-learn"
            ]
            answer = "NumPy"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        # Add new rules here...
        elif rule == "list_to_matrix_zeros_shape":
            n = random.randint(1, 5)
            m = random.randint(1, 5)
            question = f"If you want to create a matrix filled with zeros of size {n} x {m}, what function should you use in NumPy?"
            choices = [
                f"np.zeros(({n}, {m}))",
                f"np.ones(({n}, {m}))",
                f"np.matrix(({n}, {m}))",
                f"np.empty(({n}, {m}))"
            ]
            answer = f"np.zeros(({n}, {m}))"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_identity_shape":
            n = random.randint(1, 5)
            question = f"What is the shape of an identity matrix of size {n} x {n}?"
            choices = [
                f"({n}, {n})",
                f"({n}, 1)",
                f"(1, {n})",
                

            ]
            answer = f"({n}, {n})"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_diagonal_element":
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            question = f"If you have a list of diagonal elements [2, 4, 6, 8], what would be the value of the element at row {row} and column {col} in the diagonal matrix?"
            choices = [
                "2",
                "4",
                "6",
                "8"
            ]
            answer = str(2 + 2 * min(row, col))
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_transpose_shape":
            n = random.randint(1, 5)
            m = random.randint(1, 5)
            question = f"If you have a matrix of shape ({n}, {m}), what is the shape of its transpose?"
            choices = [
                f"({n}, {m})",
                f"({m}, {n})",
                f"({n}, {n})",
                f"({m}, {m})"
            ]
            answer = f"({m}, {n})"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_concatenate_shape":
            m1 = random.randint(1, 5)
            m2 = random.randint(1, 5)
            n = random.randint(1, 5)
            question = f"When concatenating two matrices horizontally, what is the shape of the resulting matrix if the first matrix has shape ({m1}, {n}) and the second matrix has shape ({m2}, {n})?"
            choices = [
                f"({m1 + m2}, {n})",
                f"({n}, {m1 + m2})",
                f"({m1}, {m2})",
                f"({n}, {n})"
            ]
            answer = f"({m1 + m2}, {n})"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_conversion_library":
            question = "Which Python library provides a `tolist()` function to convert a matrix back to a list?"
            choices = [
                "NumPy",
                "pandas",
                "matplotlib",
                "scikit-learn"
            ]
            answer = "NumPy"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
        
        elif rule == "list_to_matrix_shape_unknown":
            question = "If you have a Python list with an unknown number of elements, what is the shape of the resulting matrix when converting it to a NumPy array?"
            choices = [
                "(1, 1)",
                "(n, 1)",
                "(1, n)",
                "(n, m)"
            ]
            answer = "(n, 1)"
            random.shuffle(choices)  # Shuffle the answer choices
            questions.append((question, choices, answer))
    
    return questions

# List of rules
rules = [
    "list_to_matrix_shape",
    "list_to_matrix_access",
    "list_to_matrix_conversion",
    "list_to_matrix_zeros_shape",
    "list_to_matrix_identity_shape",
    "list_to_matrix_diagonal_element",
    "list_to_matrix_transpose_shape",
    "list_to_matrix_concatenate_shape",
    "list_to_matrix_conversion_library",
    "list_to_matrix_shape_unknown"
   
]

# Generate and print questions for each rule
num_questions_per_rule = 100
all_questions = []

for rule in rules:
    questions = generate_multiple_choice_question(rule, num_questions_per_rule)
    all_questions.extend(questions)

# Shuffle the questions to mix them up
random.shuffle(all_questions)

# Print the questions with shuffled options
for i, (question, choices, answer) in enumerate(all_questions, start=1):
    print(f"Question {i}:")
    print(question)
    # Shuffle the options for each question
    shuffled_choices = random.sample(choices, len(choices))
    for j, choice in enumerate(shuffled_choices):
        print(f"{chr(97+j)}) {choice}")
    print(f"Answer: {answer}\n")


# In[ ]:




