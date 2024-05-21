# Car Data ETL Process

This Python script performs an Extract, Transform, and Load (ETL) process for car sales data using Amazon S3 and Pandas. It extracts data from a Parquet file, transforms it, and saves the cleaned data to a CSV file.

## Prerequisites

Before running the script, ensure you have the following set up:

1. **Amazon S3 Access**: You'll need access to an Amazon S3 bucket where the Parquet file is stored.

2. **Boto3 and Pandas**: Install the required dependencies using the following command:

   ```bash
   pip install boto3 pandas
   ```

## Data Transformation

1. Renaming Columns: The script renames the column `Unique_Vehicle_Id#0` to `Unique_Vehicle_ID`.

2. Extracting Title Information: It splits the `title` column and keeps only relevant information (removing the first 3 words).

3. Selecting Relevant Columns: The cleaned data includes columns such as `vehicleid`, `Unique_Vehicle_ID`, `brand`, `year`, `model`, `title`, `usedornew`, `transmission`, `engine`, `drivetype`, `fueltype`, `fuelconsumption`, `kilometres`, `cylindersinengine`, `bodytype`, `Suburb`, `State`, `doors`, `seats`, `Exterior_Colour`, `Interior_Colour`, and `price`.

4. Saving Data: The cleaned data is saved to `final_data_fixed.csv`.
