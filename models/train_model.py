import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    X = df[['skill_match_score', 'experience_match_score', 'education_match_score', 'semantic_similarity']]
    y = df['shortlisted']
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X, y = load_data("data/candidate_features/sample_candidate_features.csv")
    X_train, X_test, y_train, y_test = split_data(X, y)

    print("Total candidates:", len(X))
    print("Training set size:", len(X_train))
    print("Testing set size:", len(X_test))
    print()
    print("Training labels distribution:")
    print(y_train.value_counts())
    print()
    print("Testing labels distribution:")
    print(y_test.value_counts())