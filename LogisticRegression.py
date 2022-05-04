 features = list(data.columns)

        features.remove('purchase')
        features.remove('buyer')
        features.remove('thank_you')
        features.remove('user_pseudo_id')

        print('features ', features)

        x = data[features]
        y = data[target]
       
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

        ## Regresión Logística
        logreg = LogisticRegression()
        logreg.fit(x_train,y_train)
        y_pred = logreg.predict(x_test)
        print('Precisión Regresión Logística: ')
        print(logreg.score(x_train,y_train))



        