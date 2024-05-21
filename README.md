# WheelsDirect

This Python script extracts data from a CSV file and loads it into a [Supabase](https://supabase.com/) table, to be viewed on [PowerBI](https://app.powerbi.com/).

## Prerequisites

Before running the script, make sure you have the following set up:

1. **Supabase Account**: You'll need a Supabase account to create a table and obtain the necessary credentials (URL and API key).

2. **Environment Variables**: Set up environment variables for your Supabase URL (`SUPABASE_URL`) and API key (`SUPABASE_KEY`). You can use a `.env` file or set them directly in your environment.

3. **CSV Data File**: Ensure you have a CSV file named `data.csv` containing the car sales data.

## Usage

1. Clone this repository or download the script.

2. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. The script will extract data from `data.csv` and upsert it into the `CarSales` table in your Supabase project.
