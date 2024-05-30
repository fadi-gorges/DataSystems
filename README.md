# WheelsDirect

This GitHub repository contains two Python scripts for managing car sales data: an ETL (Extract, Transform, Load) process and a data loader. Below is an overview of each script:

## 1. Car Data ETL Process

This script performs the following tasks:

1. **Extract**: It retrieves car sales data from an Amazon S3 bucket. You'll need to set up your S3 bucket name and file key in the script.

2. **Transform**: The script cleans the data by renaming columns, extracting relevant information from the `title` column, and selecting specific columns for further analysis.

3. **Load**: The cleaned data is saved to a CSV file (`final_data_fixed.csv`).

## 2. Car Sales Data Loader

This script extracts data from a CSV file (`data.csv`) and loads it into a [Supabase](https://supabase.com/) table named `CarSales`. It's designed to be part of a data pipeline for managing car sales data.

## 3. Car Sales Database Setup

These SQL queries create and populate the various database tables for the WheelsDirect Car Sales Analysis System. These scripts were updated and improved upon during the development process.

### You can view a more detailed README inside each folder
