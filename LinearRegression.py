
# Modelo Regresión Linear
        #Creación del modelo

        x = data[features]
        y = data[target]
       
        x_train, x_test, y_train, y_test = train_test_split(x,y)


        ## LinearRegression
        model = LinearRegression()
        model.fit(x_train, y_train)
        
        predit_train = model.predict(x_train)

        predit_test = model.predict(x_test)

        # Evaluación de R2
        print('R2 en entrenamiento es: ', model.score(x_train, y_train))
        print('R2 en validación es: ', model.score(x_test, y_test))
        
        resultado_test = model.score(x_train, y_train)