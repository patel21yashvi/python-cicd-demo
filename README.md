
# Python CI/CD Pipeline Using GitHub Actions

## Aim
To automate the build, testing, and deployment-package creation of a Python application using GitHub Actions.

## Project Description
This project demonstrates Continuous Integration and Continuous Delivery (CI/CD) using GitHub Actions. The Python application contains functions for greeting a student and adding two numbers.

## Technologies Used
- Python 3.12
- GitHub
- GitHub Actions
- pytest

## Project Structure
```text
python-cicd-demo/
├── app.py
├── test_app.py
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml
```

## Application Code
The application includes two functions:
- `greet(name)` - Returns a greeting message.
- `add(a, b)` - Returns the sum of two numbers.

## Unit Testing
The project uses pytest to test the application.

Test cases:
1. Test the greeting function.
2. Test addition of positive numbers.
3. Test addition of negative numbers.

Run tests locally using:
```bash
python -m pip install pytest
python -m pytest -v
```

## CI/CD Pipeline
The GitHub Actions workflow performs these steps:
1. Checks out the source code.
2. Sets up Python 3.12.
3. Installs pytest.
4. Builds the application by checking Python syntax.
5. Runs unit tests.
6. Prepares the deployment package.
7. Uploads the application as a GitHub Actions artifact.

## Workflow Trigger
The workflow runs automatically when code is pushed to the `main` branch or when a pull request targets `main`. It can also be started manually from the Actions tab.

## Expected Result
All three unit tests should pass, and the workflow should publish a downloadable artifact named `python-application`.

## Conclusion
GitHub Actions automates the build, testing, and packaging of the Python application. This reduces manual effort, identifies errors early, and improves the reliability of the software development process.
