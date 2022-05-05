from app.main import app
import csv
from json import load
import os
import load
from sklearn.pipeline import make_pipeline
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression,Ridge,Lasso, LogisticRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
import joblib
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from google.cloud import bigquery
from flask import Flask, make_response,render_template,  request,session, send_file, send_from_directory, current_app
import io
from io import StringIO
pd.set_option('display.max_columns', None)


  
  
app = Flask(__name__)
  
  
# reading the data in the csv file
df = pd.read_csv('data.csv')
df.to_csv('data.csv', index=None)
  


@app.route('/index.html', methods=['GET', 'POST'])
def index2():
    return render_template('index.html')



@app.route('/', methods=['GET', 'POST'])
def index():
    img_url = "https://ramonfbaeza.com/wp-content/uploads/2022/03/logo-300x127-1.png"
    return render_template('index.html',img_url=img_url)



@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_csv(file, sep=',')

        data = data.loc[(data.sum(axis=1) != 0), (data.sum(axis=0) != 0)] # Elimiamnos variales que siempre están a 0
        metrics_list = list(data.values) 
        #events_list = list(data.values)


        columns = data.columns
        columns_list = list(columns)
        print("columns_list: ", columns_list)
        
        metrics_head = data.head()
        print("metrics_head: ", metrics_head)
       
        users = data['user_pseudo_id'].count()
        sessions = data['session_start'].sum()
        first_visits = data['first_visit'].sum()
        first_visits_per = (first_visits/sessions)* 100
        first_visits_per = round(first_visits_per, 1) 
        thank_you = data['click'].sum()
        page_views = data['page_view'].sum()
            

        target = 'click'

        # discretizamos la variable objetivo
        data['buyer'] = [1 if x > 0 else 0 for x in data['click'].values]

        buyers = data['buyer'].sum()

        columns = data.columns
        columns_list = list(columns)

        features = list(data.columns)

        features.remove('click')
        features.remove('buyer')
        #features.remove('thank_you')
        #features.remove('user_pseudo_id')

        print('features ', features)

        ## CÓDIGO PARA PREDECIR EL MODELO
        x = data[features]
        y = data[target]
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

        ## Regresión Logística
        logreg = LogisticRegression()
        logreg.fit(x_train,y_train)
        y_pred = logreg.predict(x_test)
        print('Precisión Regresión Logística: ')
        print(logreg.score(x_train,y_train))
    
        result = round(logreg.score(x_train,y_train), 3) 
        print("RESULT: ", result)

        with open('model_pickle','wb') as f:
            pickle.dump(logreg,f)

        data[columns_list].to_csv('./results.csv')
        data[columns_list].to_excel('./results.xlsx',index=False)
        
        return render_template('metrics.html',result=result, x=x,y=y,users=users,data=data,metrics_head=metrics_head,columns_list=columns_list, target=target,sessions=sessions,first_visits_per=first_visits_per,page_views=page_views,thank_you=thank_you,buyers=buyers,features=features)






@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('predict.html')
    



@app.route('/transform',  methods=['GET', 'POST'])
def transform_view():
    f = request.form['upload-file']
    data = pd.read_csv(f, sep=';')

    print(f)
    if not f:
        return "No file"
    
    
    print("HELLOOOOOOO")
    print("DATA:",data)
    
    data = data.drop('click', 1)
   # data = data.drop('buyer', 1)

    # load the model from disk
    loaded_model = pickle.load(open('model_pickle', 'rb'))
    data['prediction'] = loaded_model.predict(data)
    print("ADDIOOOOOOOSS")
    
    columns = data.columns
    print("columns: ", columns)
    columns_list = ["user_pseudo_id","prediction"]

    metrics_list = list(data.values)
    
    data[columns_list].to_csv('./results.csv')
    data[columns_list].to_excel('./results.xlsx',index=False)


    for row in data.iterrows():                                                          
        for i in range(len(data.columns)):
            print(row[i])
                                                                
                        
            return render_template('table.html',data=data,titles=[''],columns_list=columns_list,metrics_list=metrics_list,columns=columns)

 

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./results.csv"
    return send_file(path, as_attachment=True)






if __name__ == '__main__':
    app.run(port=5000,debug=True) 










if __name__ == "__main__":
    app.run(debug=True) 

