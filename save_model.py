 ## CÓDIGO PARA GUARDAR EL MODELO
        X = data[features]
        Y = data[target].ravel
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)


        pipe = make_pipeline(StandardScaler(), LogisticRegression)
        pipe.fit(X_train, Y_train)
        joblib.dump(pipe, 'model.pkl')

        clf = load('filename.joblib') 