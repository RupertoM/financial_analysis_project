# Venmito Data Engineering Project

## Overview

This repository contains the code and files for a data engineering project focused on a company named "Venmito." The objective of this project was to ingest, match, conform, analyze, and present data from five different files:

- `people.json`
- `people.yml`
- `transfers.csv`
- `transactions.xml`
- `promotions.csv`

The project was implemented using Python, the Pandas library, Flask, MySQL, AWS, and a Model-View-Controller (MVC) architecture.

## Project Structure

The project is organized using the MVC methodology:

- **Model**: The model is responsible for handling data operations. It communicates with a MySQL server hosted on AWS to fetch data using SQL queries.

- **View**: The view is a simple HTML file with some vanilla JavaScript, providing a user interface for interacting with and visualizing the data.

- **Controller**: The controller handles the interaction between the user and the model. It processes user inputs, requests data from the model, and passes the information to the view for display.

- **Data Processing**: Data processing is encapsulated in `data_processor.py`, which contains logic for ingesting, matching, and conforming data.

- **Data Uploading**: `data_uploader.py` is used for pushing data into the MySQL server, ensuring the model only fetches data without manipulating it while also allowing for the ease of resetting the database at any time given that no new data was being passed in.

## Setup and Usage

1. **Install and Setup Virtual Environment:**

   - Ensure you have Python installed on your system.
   - Open a terminal and navigate to the project directory.
   - Run the following commands:

     ```bash
     # Install virtualenv using pip
     pip install virtualenv

     # Create a virtual environment named '.venv'
     python -m venv .venv
     ```

2. **Activate Virtual Environment:**

   - On Mac/Linux, activate the virtual environment:
     ```bash
     source .venv/bin/activate
     ```

3. **Install Dependencies:**

   - With the virtual environment activated, install project dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

4. **OPTIONAL: Reset Database (Not necessary as AWS server is set up):**

   - If you wish to reset the local database and see the upload, run:
     ```bash
     python app.py --reset-db
     ```

5. **Run Flask Application:**

   - Start the Flask backend server:
     ```bash
     python app.py
     ```
     Ensure the backend server is running at [http://127.0.0.1:5000](http://127.0.0.1:5000).

6. **Open the Web Interface:**

   - Open a new terminal window (while keeping the virtual environment active).
   - Run the following command to open the web interface in your default browser:
     ```bash
     open index.html
     ```
     If you prefer a different browser, copy and paste the provided link at the top of your default browser into the browser of your choosing.

7. **Interact with the Application:**

   - You can now interact with the data analysis application through the provided user interface. You will be able to see drop down selections to interact and view different analytic information.

8. **Deactivate Virtual Environment:**
   - When finished, deactivate the virtual environment:
     ```bash
     deactivate
     ```

## Data Processing Steps

1. **Ingestion:**

   - Read the data from the provided files (`people.json`, `people.yml`, `transfers.csv`, `transactions.xml`, `promotions.csv`) using Pandas.

2. **Matching and Conforming:**

   - Implement matching and conforming logic in `data_processor.py` to ensure data consistency.

3. **Analysis:**

   - Use Pandas and SQL queries to perform data analysis based on user requests.

4. **Output:**
   - Display the analyzed data on the web interface for the user to interact with.

## Usage of Data Processing Scripts

- **Data Processor (`data_processor.py`):**

  - Execute `data_processor.py` to handle data processing tasks.

- **Data Uploader (`data_uploader.py`):**
  - Run `data_uploader.py` to upload data into the MySQL server.

## Future Improvements

- **Enhanced Analytics:**

  - Consider developing additional backend analytics functions for more in-depth analysis.

- **UI Experience:**
  - Transition from vanilla JavaScript to React for a more concise codebase and improved user interface.

## Contributors

- [Your Name]

Feel free to reach out for any questions or improvements!

---

Feel free to further customize the README based on your specific details, contributors, or any additional information you find relevant. Once you are satisfied with the content, you can simply copy and paste this into the README.md file in your GitHub repository.
