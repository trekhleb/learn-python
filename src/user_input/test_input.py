"""User input

@see https://docs.python.org/3/library/functions.html#input

User input prompts are very helpful when it comes to interactive programming. Not only in games but also in standard file operations, you may want your user to interact with the program.
Therefore, the user needs the opportunity to be able to put in information.
"""


def user_input():
	""" prompt the user to enter their name and greets them"""

	# Prompt the user to enter their name
	user_name = input("Please type in your name\n")

	# Printing a greeting message
	print(f"Welcome, {user_name}!")
