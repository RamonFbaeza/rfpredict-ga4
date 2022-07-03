
![RamónFbaeza Logo](https://ramonfbaeza.com/wp-content/uploads/2022/03/logo-400x400px-e1647431977872.png)
# RF Predict Google Analytics 4

RF predict GA4 is a project built with Python using Flask. The main functionality of this project is to estimate if an user will make a purchase based on their previous behaviour. We are using Google Analytics 4 event data.

## To start 🚀

These instructions will allow you to download this project and run it **locally on your machine**.


### Requirements 📋

* Google Analytics 4
* BigQuery export enabled for your GA4 data stream 
* Flask
* Python




### Step 1.  🔧

Clone this project to your own machine

```
git clone https://github.com/RamonFbaeza/rfpredict-ga4
```

### Step 2.  🔧

Access to your folder and execute the following command to run the Flask App. 
```
python3 app.py      
```
Now yoy can navigate to the following address: http://127.0.0.1:5000/ and you should see the web app running.

![Main View](https://ramonfbaeza.com/wp-content/uploads/2022/07/rfpredict-ga4-1.png)

### Step 3.  🔧

Download your GA4 metrics from your BigQuery project (_if you have enabled BigQuery Export for your GA4 data stream_) using the following code but using your own project_id and your own events



 ```
       select
            *
          from (
            select
                user_pseudo_id,
                event_name
            from
                  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210101`)
          pivot (
            count(*)
            for
                event_name
            in (
                'session_start',
                'first_visit',
                'page_view',
                'scroll',
                'click',
                'view_search_results',
                'file_download',
                'user_engagement',
                'view_item',
                'view_promotion',
                'add_to_cart',
                'select_item',
                'begin_checkout',
                'view_search_results',
                'add_shipping_info',
                'select_promotion',
                'add_payment_info',
                'purchase',
```

        

### Step 4.  🔧

Upload your file to the web app and

![Main View](https://ramonfbaeza.com/wp-content/uploads/2022/07/rfpredict-ga4-2.png)


Then, **you will get your model trainned and you will see the model score**. You will also be able to upload a new file to predict conversion probability for each client (user_pseudo_id). **You will be able to download an excel/csv** file with all the predictions.


## Machine Learning - Logistic Regression
The model used to build this tool was the Logistic Regression from sklearn library. 

We try to predict if an user will get a conversión (purchase) based on their previous behaviour


* [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) - Model

## Built with 🛠️



* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Framework used (based on Python)
* [Python 3](https://www.python.org/downloads/) - Web Language
* [Bootstrap](https://getbootstrap.com/) - Used to build the frontend




## Authors ✒️


* **Ramón Fernández** - *Full project* - [ramonfbaeza](https://ramonfbaeza.com/sobre-mi/)





---
⌨️ Project built by [ramonfbaeza](https://ramonfbaeza.com/sobre-mi/) 😊
