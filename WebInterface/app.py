from flask import Flask, render_template, request
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import pandas as pd

model =  load("model")
tfidf_vect = TfidfVectorizer(sublinear_tf=True)
df=pd.read_csv("lemmatized_data_reduced.csv",encoding ="ISO-8859-1",names=["first_index","text","target","Text","text_final"])
df=df.iloc[1:]
tfidf_vect.fit(df['text_final'])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict',methods=["POST"])
def res():
    sentence = request.form['sentence']
    
    prediction= model.predict(tfidf_vect.transform([sentence]))
    return render_template('result.html',data=prediction[0])
    

if __name__ =="__main__":
    app.run(host='0.0.0.0')