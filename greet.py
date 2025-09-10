#!/usr/bin/env python3
"""
A simple Python script for demonstration.
"""

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to my GitHub project."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
