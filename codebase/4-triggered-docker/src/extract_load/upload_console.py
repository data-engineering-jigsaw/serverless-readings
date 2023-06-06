from request_and_upload import *

import pandas as pd

query_bucket_name = 'jigsawtexasquery'
# bucket = s3.create_bucket(Bucket = query_bucket_name)
# results_bucket_name = 'jigsawtexasresults'
# results_bucket = s3.create_bucket(Bucket = results_bucket_name)


restaurant_name = 'HONDURAS MAYA CAFE & BAR LLC'
df, file_name = request_and_download_locally(restaurant_name)
uploaded_text = upload_and_read(file_name, query_bucket_name)

