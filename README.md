# Traffic Accidents Analysis

This project analyzes traffic accidents using data from MongoDB

## Setup
- Ensure MongoDB is installed and running.
- Set up a virtual environment: `python -m venv .venv`
- Activate the environment: `source .venv/bin/activate` (Linux/macOS) or `.\.venv\Scripts\activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

## Running the Project
1. Upload CSV data to MongoDB by running `python src/data_upload.py`.
2. Create a Spark session: `python src/spark_session.py`.
3. Load data from MongoDB into Spark: `python src/data_loading.py`.
4. Process and analyze data: `python src/processing.py` and `python src/analysis.py`.
5. Visualize data: `python src/visualization.py`.

## Additional Notes
- Ensure MongoDB connection strings are correct in the scripts.
- Adjust paths and configurations as needed.