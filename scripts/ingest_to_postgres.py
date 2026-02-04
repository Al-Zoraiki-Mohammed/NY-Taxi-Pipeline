# ingest_to_postgres.py
import os
import pandas as pd
from sqlalchemy import create_engine

# Get the env vars, db host default to localhost if running outside Docker
db_host = os.getenv("DB_HOST", "localhost")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")


def load_to_postgres(year, month):
    input_file = f"./data/cleaned_taxi_{year}_{month:02d}.parquet"
    engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:5432/{db_name}")
    
    df = pd.read_parquet(input_file, engine='pyarrow')
    
    table_name = f"taxi_trips_{year}_{month:02d}"

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append', 
        index=False,
        chunksize=100000
    )
    
    print(f"Successfully loaded {len(df)} rows into '{table_name}'!")