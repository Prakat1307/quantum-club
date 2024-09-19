# Fill missing values
df.fillna(df.mean(), inplace=True)  
for column in df.select_dtypes(include=['object']).columns:
    df[column].fillna(df[column].mode()[0], inplace=True) 


df = pd.get_dummies(df, columns=['Industry', 'Series'], drop_first=True)