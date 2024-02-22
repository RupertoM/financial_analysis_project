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

## SQL Schema

### Persons Table

- **Columns:**
  - `person_id` INT PRIMARY KEY
  - `firstName` VARCHAR(100) NOT NULL
  - `surname` VARCHAR(100) NOT NULL
  - `email` VARCHAR(255) NOT NULL
  - `telephone` VARCHAR(20) NOT NULL
  - `city` VARCHAR(50) NOT NULL
  - `country` VARCHAR(50) NOT NULL
  - `Android` BOOLEAN NOT NULL
  - `iPhone` BOOLEAN NOT NULL
  - `Desktop` BOOLEAN NOT NULL

### Promotions Table

- **Columns:**
  - `promotion_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT
  - `client_email` VARCHAR(255) NOT NULL
  - `telephone` VARCHAR(20)
  - `promotion_item` VARCHAR(50) NOT NULL
  - `responded` VARCHAR(20) NOT NULL
  - `person_id` INT NOT NULL, FOREIGN KEY (person_id) REFERENCES Persons(person_id)

### Transactions Table

- **Columns:**
  - `transaction_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT
  - `person_id` INT NOT NULL, FOREIGN KEY (person_id) REFERENCES Persons(person_id)
  - `item` VARCHAR(50) NOT NULL
  - `price` DECIMAL NOT NULL
  - `store` VARCHAR(255) NOT NULL
  - `transactionDate` DATE NOT NULL

### Transfers Table

- **Columns:**
  - `transfer_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT
  - `sender_id` INT NOT NULL, FOREIGN KEY (sender_id) REFERENCES Persons(person_id)
  - `recipient_id` INT NOT NULL, FOREIGN KEY (recipient_id) REFERENCES Persons(person_id)
  - `amount` DECIMAL NOT NULL
  - `transferDate` DATE NOT NULL

## Data Analysis

1. **People Insights:**

   - *Use Case:* This option allows users to analyze data related to individuals, such as their personal information, possible connections, shopping trends, and more.

   - *Company Benefits:* Understanding customers and preferences helps Venmito tailor promotions and communication strategies, enhancing customer satisfaction and loyalty.

   - *Available Analytics:*
     - **All Promotions:** Displays all currently available promotions, including recipient information so that the viewer can get an overview.
     - **All Failed Promotions:** Lists individuals who rejected promotions along with their contact information, facilitating follow-up efforts to convert negative responses.
     - **Individuals Shopping History:** Displays data on individuals' transaction history, including purchased items and transaction details.
     - **Individuals Favorite Stores:** Highlights stores frequently visited by each individual enabling understanding of store access and item availability.
     - **Individuals Favorite Items:** Lists items purchased and favored by individuals, enabling targeted promotions.
     - **Probable Connections:** Identifies individuals likely acquainted, facilitating potential joint promotions and communications.

2. **Stores Insights:**

   - *Use Case:* Analyzing store data provides insights into store performance, popular items, profitability, promotion performance, and more.

   - *Company Benefits:* Venmito can optimize store operations, stock popular items, and improve overall store efficiency.

   - *Available Analytics:*
     - **Best Selling Stores:** Highlights stores with the highest sales.
     - **Best Selling Items:** Identifies the best-selling item across all stores and the best-selling item across each individual store.
     - **Most Profitable Items:** Lists the most profitable item across all stores and the most profitable per each store.
     - **Successful Promotion Items:** Displays items that performed well in promotions and who they succeded with.
     - **Failed Promotion Items:** Lists items that did not perform well in promotions and who they did not perform well with.

3. **General Data:**

   - *Use Case:* Provides access to general data, allowing users to view comprehensive information.

   - *Company Benefits:* Enables users to explore overall trends, patterns, and information within the dataset by having full access.

   - *Available Analytics:*
     - **All Data on People:** Provides comprehensive data on all individuals within the dataset.
     - **All Stores Data:** Displays comprehensive data on all stores.
     - **All Transfer Data:** Provides a detailed overview of all transfer transactions.
     - **All Transaction Data:** Offers a comprehensive view of all transactions.

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

4. **Run Flask Application:**

   - Start the Flask backend server:
     ```bash
     python app.py
     ```
     Ensure the backend server is running at [http://127.0.0.1:5000](http://127.0.0.1:5000).

5. **OPTIONAL: Reset Database (Not necessary as AWS server is set up):**

   - If you wish to reset the local database and see the upload, run:
     ```bash
     python app.py --reset-db
     ```

6. **Open the Web Interface:**

   - Open a new terminal window (while keeping the virtual environment active).
   - Run the following command to open the web interface in your default browser:
     ```bash
     open index.html
     ```
     If you prefer a different browser, copy and paste the provided link at the top of your default browser into the browser of your choosing.

7. **Interact with the Application:**

   - You can now interact with the data analysis application through the provided user interface. You will be able to see drop-down selections to interact and view different analytic information.

8. **Deactivate Virtual Environment:**
   - When finished, deactivate the virtual environment:
     ```bash
     deactivate
     ```
     
## Future Improvements

- **Enhanced Analytics:**

  - Consider developing additional backend analytics functions for more in-depth analysis, add search parameters or front-end filtering.

- **UI Experience:**
  - Transition from vanilla JavaScript to React for a more concise codebase and improved user interface with added functionality.

- **AI/ML Integration:**
  - Add an AI component to help with data analysis and speed up the process for company employees. Possible use cases would be finding out an individual's native language based on city and country information, translation, and possible connections between people, stores, etc.

## Contributors

- Ruperto Martinez
