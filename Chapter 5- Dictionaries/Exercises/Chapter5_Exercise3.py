## Exercise 3: Glossary 2 :ballot_box_with_check:

glossary = {
    "int": "converts the specified value into an integer number.",
    "string": "is a collection of alphabets, words or other characters.",
    "loop": "is used to execute a block of statements repeatedly until a given condition is satisfied.",
    "print": "function prints the specified message to the screen, or other standard output device.",
    "if else": "is used to execute both the true part and the false part of a given condition",
    "list": "is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.",
    "value": "is an inbuilt method in Python programming language that returns a view object.",
    "float": "is a method that returns a floating-point number for a provided number or string.",
    "boolean": "t's used to represent the truth value of an expression.",
    "comment": "is the inclusion of short descriptions along with the code to increase its readability.",
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
