# GCP-DataFlow
Automated Data Pipeline: Google Cloud Storage to BigQuery using Cloud Run Functions 

This project demonstrates an automated ETL workflow designed to transfer data seamlessly from Google Cloud Storage (GCS) to BigQuery using Cloud Functions and Cloud Run services on Google Cloud Platform.

The solution includes:

Metadata Management: JSON and Java files containing configuration parameters are manually uploaded to a dedicated metadata bucket in GCS.

Serverless Orchestration: A Python-based Cloud Function is triggered to read the metadata files, extract relevant parameters, and use them to automate the data loading process.

Data Loading: The function orchestrates the movement of raw data files stored in GCS into BigQuery tables, ensuring the process is event-driven, scalable, and repeatable.

This setup shows how Cloud Run and Cloud Functions can be integrated to create a serverless, parameterized data pipeline on GCP, enabling easier maintenance and minimal manual intervention after the initial configuration.

Tech stack: Google Cloud Storage | BigQuery | Cloud Functions | Cloud Run | Python | JSON | Java (metadata)

This project is a practical example of serverless data engineering and parameterized automation on the Google Cloud Platform.

Attached below are key screenshots from the project :
<img width="1920" height="833" alt="Source – t…-dataflow – Cloud Run – My First Project – Google Cloud console - Google Chrome 11-07-2025 13_38_22" src="https://github.com/user-attachments/assets/de8a45d4-2ed6-40d4-9972-5af00869f9f7" />
<img width="1920" height="837" alt="Source – t…-dataflow – Cloud Run – My First Project – Google Cloud console - Google Chrome 11-07-2025 13_01_01" src="https://github.com/user-attachments/assets/8e5b4e60-666d-42dc-b353-f423a03c4ac5" />
<img width="1920" height="821" alt="Source – t…-dataflow – Cloud Run – My First Project – Google Cloud console - Google Chrome 11-07-2025 12_57_33" src="https://github.com/user-attachments/assets/682285ca-bd59-4a77-894b-ca7f652fcbca" />
<img width="1920" height="826" alt="Repository – BigQuery – My First Project – Google Cloud console - Google Chrome 11-07-2025 18_05_15" src="https://github.com/user-attachments/assets/d75c5f28-e6fc-4e58-b9ae-542ca591b023" />



