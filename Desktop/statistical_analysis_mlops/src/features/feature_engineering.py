def create_features(df):
    df['new_feature'] = df['existing_feature'] * 2
    return df
