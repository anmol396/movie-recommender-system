def preprocess(df):
    features = ['genres','keywords','tagline','cast','director']
    
    for feature in features:
        df[feature] = df[feature].fillna('')
    
    return df