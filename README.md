# ML-customer-conversion
ML zoomcamp 2025 - midterm project

This project develops a machine learning pipeline to predict customer conversion likelihood based on lead behavior and demographic data. 

The model identifies high-potential leads to optimize marketing strategies and improve conversion rates.

## Data
This project uses a synthetic dataset from Kaggle:
👉 [Customer Conversion Prediction Dataset](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-conversion-dataset-for-stuffmart-com?select=customer_conversion_traing_dataset+.csv)

Only the training dataset is used for this project.

🎯 Target Variable

- `converted` — Binary indicator of customer conversion
(`1` = converted, `0` = not converted)

🔑 Key Feature Categories

- Demographics: Age, gender, location (major cities in Pakistan)

- Lead Information: Lead source, lead status, referral sources

- Engagement Metrics: Email interactions, social media engagement, form submissions

- Behavioral Data: Click-through rates, response times, downloads, follow-up emails

- Technical: Device type, payment history


## 📁 Project Structure
```bash
├── README.md                # Project documentation (this file)
├── data                     # Data folder
│ ├── data.csv               # Main dataset used for training
│ └── raw                    # Raw datasets downloaded from Kaggle
├── notebook.ipynb           # Main notebook for data exploration & model selection
├── train.py                 # Script to train and save the final model
├── predict.py               # Prediction logic used by the FastAPI service
├── model_xgb.pkl            # Trained XGBoost model + DictVectorizer
├── feature_importance.ipynb # Notebook exploring model feature importances
├── Dockerfile               # Docker setup for deploying the FastAPI service
├── get_demo_row.py          # Script to generate a demo customer record
├── demo_row.json            # Generated sample input record for testing
├── predict-demo.py          # Script to send a prediction request to the API
├── pyproject.toml           # Project dependencies + build config for uv
└── uv.lock                  # uv lockfile to maintain reproducible environments
```

## 🚀 How to Run the Project

### 1. Download the Dataset
You can either download the dataset directly from its [Kaggle webpage](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-conversion-dataset-for-stuffmart-com?select=customer_conversion_traing_dataset+.csv), or follow the steps below to download it using the Kaggle API (requires Kaggle API setup).

```bash
# Move to project directory
cd ML-customer-conversion

# Download from Kaggle
curl -L -o data/download.zip https://www.kaggle.com/api/v1/datasets/download/muhammadshahidazeem/customer-conversion-dataset-for-stuffmart-com

# Unzip
unzip data/download.zip -d data/raw/

# Rename the training dataset for convenience
cp "data/raw/customer_conversion_traing_dataset .csv" data/data.csv

# Remove zip file after extraction
rm data/download.zip
```

After downloading, the dataset is **renamed** to `data/data.csv` for convenience and easier reference throughout the project.

### 2. Train the final Model

Run the training script:

```bash
python train.py
```
This will:

- Load the dataset
- Train the final model
- Save the model and DictVectorizer to the root directory

### 3. Build and Run the Dockerized API Service

Make sure Docker is installed and running.

**Build the Docker image**:
```
docker build -t customer-api .
```

**Run the container**:
```
docker run -d -p 9696:9696 --name customer-api-container customer-api
```

The API will be available at:
http://localhost:9696/predict

### 4. Generate a Demo Customer Record
```
python get_demo_row.py
```

This will produce a sample customer dictionary for testing.

![Get a demo record](/screenshot/demo_row.png)

### 5. Test the Prediction API
With the Docker container running, call the prediction service using:
```
python predict-demo.py
```

![Prediction](/screenshot/prediction.png)

This script will send the demo customer record to the FastAPI backend and print the prediction result.

## Acknowledgments

- **ML Zoomcamp**: This project was created as part of the [ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master) mid-term assignment.  
- **Dataset**: Customer Conversion Prediction dataset, sourced from [Kaggle](https://www.kaggle.com/).  

Feel free to explore the code, run the demos, and suggest improvements! 😊
