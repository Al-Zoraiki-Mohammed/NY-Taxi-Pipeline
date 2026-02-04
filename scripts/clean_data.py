"""
Clean data and write it back.
"""
import pandas as pd


def clean_data(year, month):
    local_raw = f"./data/raw_taxi_{year}_{month:02d}.parquet"
    output_file = f"./data/cleaned_taxi_{year}_{month:02d}.parquet"
    df = pd.read_parquet(f'{local_raw}', engine='pyarrow')

    # 1. Remove obvious outliers and invalid data
    df_cleaned = df[
        (df['passenger_count'] > 0) & 
        (df['trip_distance'] > 0) & 
        (df['fare_amount'] > 0)
    ].copy()

    # 2. Convert durations to a usable format (e.g., minutes)
    df_cleaned['trip_duration_minutes'] = (
        df_cleaned['tpep_dropoff_datetime'] - df_cleaned['tpep_pickup_datetime']
    ).dt.total_seconds() / 60

    # 3. Filter out unrealistic trips (e.g., trips > 24 hours or < 1 minute)
    df_cleaned = df_cleaned[df_cleaned['trip_duration_minutes'].between(1, 1440)]

    # 4. Save the cleaned version back to Parquet
    df_cleaned.to_parquet(f'{output_file}', index=False)
