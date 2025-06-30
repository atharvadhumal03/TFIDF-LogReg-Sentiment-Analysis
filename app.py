import pickle
import streamlit
from function import full_text_preprocessing

docs = ["i Hate T!his @movie so 2332much", "i lo00ve thiS! moviE", "1this was ??suCh a waS$te of 8time", "tHi$$S was niCe ill be BaCk"]

X_new = full_text_preprocessing(docs)
print(X_new)

with open("model.pkl", "rb") as file:
    pipeline = pickle.load(file)


new_pred = pipeline.predict(X_new)
print(new_pred)