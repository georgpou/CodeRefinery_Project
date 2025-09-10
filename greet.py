#!/usr/bin/env python3
"""
A simple Python script for demonstration.
"""

def greet(name: str) -> str:
    # Return a personalized greeting string using an f-string
    return f"Hello, {name}! Welcome to my GitHub project."

if __name__ == "__main__":
    # Prompt the user for their name
    user = input("Enter your name: ")
    
    # Print the greeting returned by greet()
    print(greet(user))
