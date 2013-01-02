project_id = '787455367277'
gs_bucket_name = 'mlab-ns'
bigquery_dataset_id = 'mlabns'
bigquery_table_id = 'lookup'
bigquery_schema = [
    {
        "name":"tool_id",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"policy",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"user_ip",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"is_ipv6",
        "type":"BOOLEAN",
        "mode":"REQUIRED",
    },
    {
        "name":"user_city",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"user_country",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"user_latitude",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"user_longitude",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"slice_id",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"server_id",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"server_ip",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"server_fqdn",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"site_id",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"site_city",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"site_country",
        "type":"STRING",
        "mode":"REQUIRED",
    },
    {
        "name":"site_latitude",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"site_longitude",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"distance",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"log_time",
        "type":"INTEGER",
        "mode":"REQUIRED",
    },

    {
        "name":"latency",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"user_agent",
        "type":"STRING",
    }
]
