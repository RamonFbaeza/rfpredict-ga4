import csv
import os

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from google.cloud import bigquery
pd.set_option('display.max_columns', None)


from google.cloud import bigquery
            
credentials_path = 'python-bq-tfm/sa2-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

bqclient = bigquery.Client()

query_string = """

    SELECT
        distinct event_name,
        count(*)

    FROM
      `ramonfbaeza-ga4.analytics_245414605.events_2021*`
      
    

    GROUP BY event_name
    order by 2 desc


    """

dataframe_events = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(
            # Optionally, explicitly request to use the BigQuery Storage API. As of
            # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
            # API is used by default.
            create_bqstorage_client=True,
        )
    )


def show_events():
    
    df_events = pd.DataFrame(dataframe_events)
    return df_events

df_events = show_events()


