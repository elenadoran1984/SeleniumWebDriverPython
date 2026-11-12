# Selenium WebDriver Automation with Python

A beginner-friendly web automation project using **Python, Selenium WebDriver and Pytest**.

The project automates a DuckDuckGo search and validates the search results using the **Page Object Model (POM)** design pattern.

## Technologies

- Python
- Selenium WebDriver
- Pytest
- Pipenv
- Page Object Model (POM)

## Project Structure

```text
SeleniumWebDriverPython/
├── pages/
│   ├── search.py
│   └── result.py
├── tests/
│   ├── conftest.py
│   └── test_search.py
├── config.json
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Features

- Automated DuckDuckGo search
- Page Object Model implementation
- Pytest fixtures
- Chrome, Firefox and Headless Chrome configuration
- Explicit and implicit waits
- Selenium Manager for automatic driver management

## Installation

Clone the repository:

```bash
git clone https://github.com/elenadoran1984/SeleniumWebDriverPython.git
cd SeleniumWebDriverPython
```

## Run Tests

```bash
pipenv run python -m pytest
```

To see test output:

```bash
pipenv run python -m pytest -s
```

To run parallel tests:

```bash
pipenv run python -m pytest -n 3
```

## Author

**Elena Doran**

[GitHub Repository](https://github.com/elenadoran1984/SeleniumWebDriverPython)
