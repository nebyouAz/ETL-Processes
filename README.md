<b>Introduction</b>

A startup named Sparkify aims to analyze the data collected on songs and user activity within their new music streaming app. 

The analytics team is specifically focused on understanding user song preferences.
The project involves creating a Microsoft SQL Database Schema on Azure and an ETL (Extract, Transform, Load) pipeline to optimize queries for song play analysis

<b>Project Description </b>

This project involves modeling data with Microsoft SQL Database and building an ETL pipeline using Python. On the database side, fact and dimension tables are defined for a Star Schema with a specific focus. The ETL pipeline transfers data from files in two local directories into these tables in Microsoft SQL Database using Python and SQL.

<b>Schema for Song Play Analysis</b>

<b>Fact Table</b>

<b> songplays </b> records in log data associated with song plays

<b>Dimension Tables</b>

<b> users </b> in the app

<b> songs </b> in music database

<b> artists </b> in music database

<b> time: </b> timestamps of records in songplays broken down into specific units

<b>Project Design</b>

The database design is optimized, requiring a minimal number of tables and specific joins to extract the most information for analysis.

The ETL design is simplified, involving reading JSON files, parsing them accordingly, and storing the data into specific columns with proper formatting.

<b>Database Script</b>

Running the command `python create_tables.py` in the terminal facilitates the creation and recreation of tables.

<b>Jupyter Notebook</b>

etl.ipynb: A Jupyter notebook provided for verifying each command and data. The statements from this notebook are copied into etl.py, which can be run in the terminal using the command python etl.py. Afterward, running test.ipynb verifies whether data has been successfully loaded into all tables.

<b>Relevant Files Provided </b>

<b>test.ipnb </b>Displays the first few rows of each table, allowing you to check your database

<b>create_tables.py </b>Drops and creates your tables

<b>etl.ipynb </b>Reads and processes a single file from song_data and log_data, loading it into your tables in a Jupyter notebook

<b>sql_queries.py </b>Contains all the T-SQL queries and is imported into the last three files above