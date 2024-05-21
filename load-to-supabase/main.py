import csv
import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

class App:
    def __init__(self):
        self.supabaseUrl = os.environ.get("SUPABASE_URL")
        self.supabaseKey = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(self.supabaseUrl, self.supabaseKey)
        
        self.data = self.extract_data()
        self.load_data()

    def extract_data(self):
        print('Extracting data from CSV file...')
        
        data = []
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                newRow = dict(row)
                
                newRow['year'] = int(row['year']) if row['year'] else None
                newRow['engine'] = float(row['engine']) if row['engine'] else None
                newRow['fuelConsumption'] = float(row['fuelConsumption']) if row['fuelConsumption'] else None
                newRow['kilometres'] = int(row['kilometres']) if row['kilometres'] else None
                newRow['cylindersInEngine'] = float(row['cylindersInEngine']) if row['cylindersInEngine'] else None
                newRow['doors'] = int(row['doors']) if row['doors'] else None
                newRow['seats'] = int(row['seats']) if row['seats'] else None
                newRow['price'] = int(row['price']) if row['price'] else None
                
                data.append(dict(newRow))
                
        print(f"Extracted {len(data)} records\n")
        return data
    
    def load_data(self):
        print('Loading data to Supabase...')
        self.supabase.table('CarSales').upsert(self.data).execute()
        print('Data loaded successfully\n')

if __name__ == '__main__':
    app = App()