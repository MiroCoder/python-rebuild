# Day 9 — Modules + Imports

# Import specific functions
from helpers.utils import add, multiply

# Import a module with an alias
from helpers import utils as u

# Import through a package __init__.py
from services import get_user


if __name__ == "__main__":
    print(add(2, 3))
    print(multiply(4, 5))
    print(u.multiply(4, 5))
    print(get_user())
