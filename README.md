# Python Code Katas

## Introduction

Coding katas are short, repeatable programming challenges to help you practice your coding skills. This project provides several katas in Python, each with its own test file. You will implement each kata by following the instructions in the corresponding Python file.

## Getting Started

### Prerequisite: Install Git

If you don't have git installed, please install it first:

- On Ubuntu/Debian:
  ```bash
  sudo apt-get update
  sudo apt-get install git
  ```
- On MacOS (with Homebrew):
  ```bash
  brew install git
  ```
- On Windows: Download and install from [git-scm.com](https://git-scm.com/)

### (Optional) Install GitHub Desktop

If you prefer a graphical interface for git, you can use GitHub Desktop:

1. Download and install GitHub Desktop from [desktop.github.com](https://desktop.github.com/)
2. Open GitHub Desktop and sign in with your GitHub account.
3. To add your cloned repository:
    - Click on "File" > "Add Local Repository..."
    - Browse to the folder where you cloned this project (e.g., `katas`)
    - Click "Add Repository"
4. You can now manage your branches, commits, and pushes via the GitHub Desktop interface.

### 1. Clone the Repository

```bash
git clone git@github.com:alimulondo/python-code-katas.git katas
cd katas
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Development Branch

Before you start coding, create and switch to a branch called `dev`:

```bash
git checkout -b dev
```

## Exercise Order

Please complete the exercises in the following order:

1. FizzBuzz (`src/katas/fizz_buzz.py`)
2. Prime Factors (`src/katas/prime_factors.py`)
3. Read/Write JSON (`src/katas/read_write_json.py`)
4. Roman Numerals (`src/katas/roman_numerals.py`)
5. String Calculator (`src/katas/string_calculator.py`)
6. Unique String Finder (`src/katas/unique_string_finder.py`)
7. Env Secret Generator (`src/katas/env_secret_generator.py`)
8. Array Diff (`src/katas/array_diff.py`)

Open each file and follow the beginner-friendly instructions inside. Write your solution in the space provided.

## Running Tests

Each kata has its own test file in the `tests/` directory. You can run all tests or a single test file.

### Run All Tests

```bash
python -m unittest discover tests -p '*_test.py'
```

### Run an Individual Test

For example, to run only the FizzBuzz tests:

```bash
python -m unittest tests/fizz_buzz_test.py
```

Replace `fizz_buzz_test.py` with the test file you want to run.

## Submitting Your Work

After you finish all exercises, you can commit your changes and push your `dev` branch to your fork or repository.

```bash
git add .
git commit -m "Complete code katas"
git push origin dev
```

---

Happy coding! If you get stuck, read the instructions in each file carefully and try running the tests for hints.
