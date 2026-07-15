from extract import extract_data
from profiler import profile_data
from transform import transform_data

df = extract_data()

profile_data(df)

cleaned_df = transform_data(df)