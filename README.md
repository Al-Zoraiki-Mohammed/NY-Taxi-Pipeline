#  NY Taxi Data Engineering Pipeline (Learning Project)
* This project is a containerized ETL (Extract, Transform, Load) pipeline. It is designed to practice modern data orchestration by ingesting NYC Taxi Trip records into a PostgreSQL database.

## Learning Objective:
* This project focuses on modular Python code, container orchestration with Docker, and efficient package management using uv.

*  Project Structure & Workflow
Unlike simple scripts, this pipeline is split into functional modules orchestrated by a central controller. This separation of concerns is a professional best practice.

- pipeline.py (The Orchestrator): The entry point. It accepts user arguments (Year/Month) and coordinates the flow between the specialized scripts.

- scripts/extract_data.py: Fetches the raw data (usually from the NYC TLC Parquet/CSV sources).

- scripts/clean_data.py: Performs data validation, handles missing values, and ensures data types are correct for SQL.

- scripts/ingest_to_postgres.py: Manages the database connection and streams the cleaned data into PostgreSQL.

##  Powered by uv
- I chose uv as the package manager for this project.

- Why? It is significantly faster than standard pip.

- Reproducibility: It uses a uv.lock file to ensure that every time the Docker image is built, the exact same library versions are installed.

- Efficiency: It handles the complex Python 3.13 environment setup inside the container seamlessly.

##  How to Run
 1. Start the Database Environment

- We use Docker Compose to spin up the database and the management GUI.

- Bash> docker compose up -d pgdatabase pgadmin
2. Run the Modular Pipeline

- Because the pipeline is versatile, you tell it exactly what data to process. You don't need to change the code to change the date.

- Example: Process January 2024

- Bash> docker compose run --rm taxi_pipeline --year 2024 --month 1
* How it works under the hood:

- Docker passes the --year and --month flags to pipeline.py.

- pipeline.py triggers the Extract script to download the file.

- The Clean script processes the file in the /app/data volume.

- The Ingest script pushes the results to the pgdatabase service.

## Pro Tip: Automation

- If you want to ingest an entire year of data, you don't need to run the command 12 times manually. You can use a simple loop in your terminal:

- Bash> for m in {1..12}; do docker compose run --rm taxi_pipeline --year 2024 --month $m; done
