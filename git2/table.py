from google.cloud import bigquery 

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "firstdata-465210.Hr.p_emp"

schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("phone", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("sal", "INTEGER", mode="REQUIRED")
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.

print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)
