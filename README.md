# StepsAI NLP Intern Assessment Project

## Overview

This project involves extracting content from selected textbooks, creating a vector database using MILVUS with RAPTOR indexing, and developing a question-answering system using an LLM (Language Model). The following instructions will guide you on how to set up and run the application.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- Virtual environment tool (e.g., `venv`)

## Setup Instructions

1. **Activate Virtual Environment**

    Navigate to the `app/scripts` directory and activate the virtual environment.

    ```sh
    python -m venv app

    app/scripts/activate
    ```

2. **Install Dependencies**

    Install the required Python packages using `pip` and the `requirements.txt` file.

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**

    Execute the `watcher.py` script, which monitors file changes and restarts the process as needed.

    ```sh
    python watcher.py
    ```

## Project Structure

- `app/`: Contains the main application code.
- `app/scripts/`: Contains scripts for setting up and running the application.
- `requirements.txt`: Lists the Python dependencies needed for the project.
- `watcher.py`: Script to monitor file changes and restart the process automatically.

## Additional Information

For detailed information on the implementation and usage of the project components, please refer to the comments and documentation within the source code files.


---

Thank you for your interest in my project!
