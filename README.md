# Batch Streaming Project on AWS - Weather Data :cloud:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

### Technologies and Services Used
- Python
- Various AWS Services: EC2, Lambda, S3, Glue, Glue Catalog, Redshift, Cloudwatch, EventBridge
- Linux + Bash Commands
- API: Open Meteo - https://open-meteo.com/

## Purpose? Why?
The goal of this data engineering project was to pull in forecast data (7 days at a time) daily, and to store it in a data warehouse for future analysis. In order to perform this ETL project, we will be using AWS cloud services.

## Extraction
### API: Open Meteo Overview
"Open-Meteo is an open-source weather API with free access for non-commercial use. No API key is required." - documentation.
We will be using Open Meteo to pull relevant weather data.

![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/weatherapi.PNG)

### Python Scripting + Lambda Function
In order to pull data from this API, we will be triggering a Lambda Function via EventBridge (The lambda code is located in this repository).
The Lambda function brings in the weather data and converts the JSON data to a CSV file, all while tranforming and manipulating the data. The Lambda function then finally pushes the CSV into a S3 Bucket.

![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/lambda.PNG)
![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/lambda%20code.PNG)

### AWS Glue + Glue Catalog
Once we have the data in the S3 Bucket, we move on to using Glue. We create crawlers within Glue which extract our CSV file from S3, and then create tables in a Glue Catalog. This happens daily, so the Catalog is always up to date. 

![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/s3bucket%20dynamic%20title.PNG)
![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/crawlers.PNG)
![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/glue%20catalog.PNG)

### Glue to Redshift
Once we have the Glue Catalogs / Tables complete, we then use Glue once again to move the data to Redshift. We create an automatic Glue Job that moves the cataloged Glue data to Redshift.

![alt text](https://github.com/airincs/batch-project-weather/blob/main/images/redshift%20weather.PNG)
