# Notes

## Key concepts and topics

### Chapter 1

- Installing Python and pytest
- Creating a new Python project
- Writing the first test case

## Tips and tricks

1. Properly installing Python can be complicated, especially if Python was previously installed on your machine. Make sure to follow appropriate instructions for your operating system and verify your installation with the command python --version (or python3 --version if needed).

2. When creating a new Python project for pytest tests, it's conventional to create a directory named "tests" to separate product code from test code. However, when writing new test cases on your own, you might want to add them to an existing project rather than creating an entirely new project.

3. To run tests from the command line using pytest, enter the command python -m pytest from the project's root directory. This will find and execute all test cases within the project. Note that you can also use the shorter pytest command, but it's recommended to use python -m pytest to automatically add the current directory to sys.path.

## Errors and solutions

### Errors

- If Python is not installed properly, the command "python --version" may not work and the expected version number may not be printed. In such cases, using "python3 --version" may work instead.
- If the correct Python installation is not included in the system path, Python may not work. To fix this, find the directory into which Python was installed, manually add it to the system path if it is not already included, and relaunch the command line.
- When running tests using "python -m pytest", if the tests fail, double-check the code and setup to identify any errors.

### Solution

- To ensure that Python is installed properly, follow appropriate instructions for your operating system while installing Python. If you face issues while verifying your Python installation, use "python3 --version" instead of "python --version".
- To include the correct Python installation in the system path, find the directory into which Python was installed, and manually add it to the system path if it is not already included. To view the current path settings, use the command "echo $PATH".
- If the tests fail, double-check the code and setup for any errors. Make sure that you have installed the latest version of Python and pytest and that you have created the project directory and test case module correctly.

## Best practices

- Follow appropriate instructions for installing Python on your machine and verify the installation using the command "python --version".
- Use virtual environments to manage dependencies per project and use the "pip3" command instead of "pip" if you need to use the "python3" command to run Python.
- Stick to naming conventions in pytest by prefixing test module and test function names with "test\_" and placing them in a directory named "tests". Use the "assert" statement for performing assertions and run tests from the command line using the "python -m pytest" command.

## Resources and references

- Python official website: <https://www.python.org/>
- Pytest official website: <https://docs.pytest.org/en/latest/>
- Visual Studio Code: <https://code.visualstudio.com/>
- PyCharm: <https://www.jetbrains.com/pycharm/>
  Atom: <https://atom.io/>
- Notepad++: <https://notepad-plus-plus.org/>
- Python virtual environments: <https://docs.python.org/3/library/venv.html>
- Pytest quick start guide: <https://docs.pytest.org/en/latest/getting-started.html>
- Pytest documentation: <https://docs.pytest.org/en/latest/contents.html>
