import difflib

def recommend(movie_name, df, similarity):
    titles = df['title'].tolist()
    
    match = difflib.get_close_matches(movie_name, titles)
    
    if not match:
        return ["Movie not found"]
    
    index = df[df.title == match[0]].index[0]
    
    scores = list(enumerate(similarity[index]))
    sorted_movies = sorted(scores, key=lambda x: x[1], reverse=True)
    
    return [df.iloc[i[0]]['title'] for i in sorted_movies[1:11]]