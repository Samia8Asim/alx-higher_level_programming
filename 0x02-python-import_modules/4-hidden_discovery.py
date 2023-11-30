#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden = dir(math)
    names = [name for name in hidden if not name.startswith('__')]
    print(name)
