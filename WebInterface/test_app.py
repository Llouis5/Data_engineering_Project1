import unittest
import requests
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class TestApp(unittest.TestCase):
    

    def test_home_page(self):
        req=requests.get('http://localhost:5000')
        self.assertEqual(req.status_code, 200)

    def test_model(self):
        model =  load("model")
        tfidf_vect = TfidfVectorizer(sublinear_tf=True)
        df=pd.read_csv("lemmatized_data_reduced.csv",encoding ="ISO-8859-1",names=["first_index","text","target","Text","text_final"])
        df=df.iloc[1:]
        tfidf_vect.fit(df['text_final'])
        prediction= model.predict(tfidf_vect.transform(["Great"]))
        #2 means Positive
        self.assertEqual(prediction[0],2)

    

        

