import sys
import argparse
from scripts.extract_data import extract_data
from scripts.clean_data import clean_data
from scripts.ingest_to_postgres import load_to_postgres

def run_pipeline(year, month):
    try:
        print(f"--- Starting Pipeline for {year}-{month:02d} ---")
        
        print(f"Step 1: Extracting data for {year}/{month}...")
        extract_data(year, month)
        
        print("Step 2: Cleaning data...")
        clean_data(year, month)
        
        print("Step 3: Ingesting to Postgres...")
        load_to_postgres(year, month)
        
        print(f"✅ Pipeline completed successfully for {year}-{month:02d}!")
        
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # This block now listens to the arguments from Docker Compose
    parser = argparse.ArgumentParser(description='NY Taxi Data Pipeline')
    
    # These match the flags you put in your 'command' section
    parser.add_argument('--year', type=int, required=True, help='Year to process (YYYY)')
    parser.add_argument('--month', type=int, required=True, help='Month to process (MM)')
    
    args = parser.parse_args()
    
    # Pass the dynamic values to your function
    run_pipeline(year=args.year, month=args.month)
