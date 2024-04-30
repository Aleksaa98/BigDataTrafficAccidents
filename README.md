# Traffic Accidents Analysis

This project analyzes traffic accidents using data from MongoDB connected with Mongo Spark Connector

## Setup
- Ensure MongoDB is installed and running.
- Ensure Python is installed and running.
- Pyspark will be also installed 
- pip install py4j==0.10.9
- pip install pyspark==3.1.2
- Install dependencies: `pip install -r requirements.txt`

## Running the Project
1. Upload CSV data to MongoDB by running `python src/data_upload.py`.
2. Everything else will be done by running: `python src/analysis.py`.
3. For manualy fixing data run: `python src/NumbericType.py`.

## Additional Notes
- Ensure MongoDB connection strings are correct in the scripts.

## Screenshots
- **Screenshot 1**:
  ![Screenshot of the first feature](../data/screenshots/img 1)

- **Screenshot 2**:
  ![Screenshot of the second feature](../data/screenshots/img 2)