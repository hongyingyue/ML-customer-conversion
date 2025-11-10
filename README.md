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
  
### 📥 Get the data
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