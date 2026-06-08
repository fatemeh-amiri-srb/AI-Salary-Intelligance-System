from src.preprocessing import preprocess_tabular
from src.text_features import TextFeatureExtractor
from src.encode import CategoricalEncoder
from scipy.sparse import hstack


def build_features(df):

    # 1. tabular features
    X_tabular = preprocess_tabular(df)

    # 2. categorical encoding
    cat_encoder = CategoricalEncoder()
    X_cat = cat_encoder.fit_transform(X_tabular)

    # 3. text features
    text_extractor = TextFeatureExtractor(max_features=200)
    X_text = text_extractor.fit_transform(df)

    # 4. merge all features
    X_final = hstack([X_cat, X_text])

    return X_final, cat_encoder, text_extractor