def combine_features(df):
    df['combined_features'] = (
        df['genres'] + ' ' +
        df['keywords'] + ' ' +
        df['tagline'] + ' ' +
        df['cast'] + ' ' +
        df['director']
    )
    return df