import fsspec
import pyarrow.parquet as pq

def extract_data(year, month):
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
    local_raw = f"./data/raw_taxi_{year}_{month:02d}.parquet"
    
    with fsspec.open(url) as f:
        table = pq.read_table(f)
        pq.write_table(table, local_raw)
    print(f"✅ Raw data saved to {local_raw}")
