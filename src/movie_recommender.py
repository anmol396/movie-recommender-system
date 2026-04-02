from src.data_loader import load_data
from src.preprocessing import preprocess
from src.feature_engineering import combine_features
from src.model import vectorize, compute_similarity
from src.recommend import recommend

def main():
    df = load_data("data/movies.csv")
    
    df = preprocess(df)
    df = combine_features(df)
    
    vectors = vectorize(df)
    similarity = compute_similarity(vectors)
    
    movie = input("Enter movie name: ")
    
    results = recommend(movie, df, similarity)
    
    print("\nRecommendations:")
    for i, r in enumerate(results):
        print(i+1, r)

if __name__ == "__main__":
    main()