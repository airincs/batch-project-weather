import json
import requests
import pandas as pd
from datetime import date
import boto3
from io import StringIO
#import s3fs

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'airinfisher98-weather-raw'
    
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=Asia%2FTokyo"

    response = requests.get(url)
    weather = response.json()["daily"]

    today = date.today()

    df = pd.DataFrame(weather.values())
    df = df.T
    df.columns = ['time', 'weathercode', 'temperature_2m_max', 'temperature_2m_min', 'apparent_temperature_max', 'apparent_temperature_min', 'sunrise', 'sunset',
              'uv_index_max', 'precipitation_sum', 'rain_sum', 'showers_sum', 'snowfall_sum', 'precipitation_hours', 'precipitation_probability_max']
    df['date_pulled'] = today
    #df.to_csv(f's3://airinfisher98-weather-raw/weather{today}.csv', index=False)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, f'weather{today}.csv').put(Body=csv_buffer.getvalue())
    #df.to_csv(f'/tmp/weather.csv', index=False)
    #s3.put_object(Filename = '/tmp/weather.csv', Key = '/tmp/weather.csv', )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
