
from googleapiclient.discovery import build

def trigger_df_job(cloud_event, environment):   
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-trigger-load-unique",  # ✅ Must be unique each run!
        "parameters": {
            "inputFilePattern": "gs://bucket-for-landing-zone/users.csv",
            "JSONPath": "gs://bucket-for-meta-data/bq.json",
            "outputTable": "hallowed-kiln-465515-i8:user_data.users",
            "bigQueryLoadingTemporaryDirectory": "gs://bucket-for-meta-data/temp/",
            "javascriptTextTransformGcsPath": "gs://bucket-for-meta-data/udf.js",
            "javascriptTextTransformFunctionName": "transform"
        }
        
    }

    request = service.projects().templates().launch(
        projectId=project,
        gcsPath=template_path,
        body=template_body
    )
    response = request.execute()
    print(response)
