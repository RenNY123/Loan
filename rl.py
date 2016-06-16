
def convert_to_binary(df, column_to_convert):
    categories = list(df[column_to_convert].drop_duplicates())
    for category in categories:
        cat_name = str(category).replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace("-", "").lower()
        col_name = column_to_convert[:5] + '_' + cat_name[:10]
        df[col_name] = 0
        df.loc[(df[column_to_convert] == category), col_name] = 1

    return df
    
    
#clean the cata, eliminate null value and outliers
def reject_outliers(data, m=3):
    return data[abs(data - np.mean(data)) < m * np.std(data)]
    
def missingToMean(data):
    return data.fillna(np.mean(data))   

#create dummy variables (one hot key conversion)


    
def perfmetrics(model, test, target):
    pred = model.predict(test)
    TP, TN, FP, FN = 0, 0, 0, 0
    for i in range(0, len(test)):
        if 0.9 < pred[i] < 1.1:
            if 0.9 < target[i] < 1.1:
                TP += 1
            else:
                FP += 1
        else:
            if -0.1 < target[i] < 0.1:
                TN += 1
            else:
                FN += 1
    return (TP, TN, FP, FN)
