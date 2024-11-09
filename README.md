# Calculator-218-midterm

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
  - [Design Patterns](#design-patterns)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Available Commands](#available-commands)
  - [Examples](#examples)
- [Testing](#testing)
- [License](#license)

## Introduction

Welcome to the **Calculator Application**! This is a robust, command-line based calculator designed to perform basic arithmetic operations, manage operation history, and support undo functionality. Built with Python, this application leverages design patterns to ensure maintainability and scalability.

## Features

- **Arithmetic Operations**: Perform addition, subtraction, multiplication, division, power, and modulus operations.
- **History Management**: Keep a record of all executed operations with the ability to view, undo, and clear history.
- **Undo Functionality**: Revert the last executed operation.
- **Comprehensive Logging**: Detailed logs are maintained for monitoring and debugging purposes.
- **Extensible Architecture**: Designed using design patterns to facilitate easy addition of new features.

## Architecture

The Calculator Application is structured into modular components, each responsible for specific functionalities. This separation of concerns enhances the application's maintainability, scalability, and testability.

### Design Patterns

#### Command Pattern

The application employs the **Command Pattern** to encapsulate all information needed to perform an action or trigger an event. This pattern is instrumental in implementing features like undo operations and history tracking.

- **Classes Involved**:
  - `OperationCommand`: Represents a single operation performed by the user.
  - `HistoryManager`: Maintains a list of `OperationCommand` instances, allowing operations to be recorded and undone.
  - `CommandProcessor`: Processes user inputs, executes operations using the `Calculator`, and interacts with `HistoryManager`.

**Impact**:
- **Extensibility**: Easily add new operations without altering existing codebase.
- **Maintainability**: Clear separation between command execution and command management.
- **Undo Capability**: Simplifies implementing undo operations by maintaining a history of executed commands.

## Setup Instructions

### Prerequisites

- **Python 3.7+**: Ensure that Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

- **Setup Virtual Environment**: python -m venv venv

- **Activate virtual environment**: source venv/bin/activate

- **Install packages**: pip install -r requirements


### Installation

### Video 

https://youtu.be/7cLnFn2dWkA
