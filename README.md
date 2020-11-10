# Data_engineering_Project1
Data_engineering_Project1 for M2 course

Trello: https://trello.com/b/Ekn4hWBx/data-engineering-ii

Project included :
-Creation of a sentiment analyser in python with a score > 0.8 
-Creation of a webinterface for a user to try the model
-Docker containarization for easy export
-make unit tests 


1) SVM model
The model was created using tweets starting from this january about the corona virus (classified from "Severy Negative" to "Really Positive")
After cleaning the dataset with removing stopwords, non-alpha characters...
I saved the new data(7000 of tweets for each emotion(Neg,Neu,Pos) in an another csv.
I tried using naives bayes - Random Forest & SVM, SVM was the best out of all of them so I saved it as "model"

2) The Webinterface
The Webinterface is simple using simple html code and Jinja for the model to display the right info:
Upon arriving to the page, the user can press the button and check its answer. One amelioration could have been to add limitations to what the user can enter (i.e: no numbers)
Upon pressing the button, the user goes to another page getting the result of his prediction

3) Unfortunately the container doesn't seem to work. Everything is built without problems, the app.py is ran correctly, however, upon going to 0.0.0.0:5000 , it doesn't work.
Even for localhost:5000 

4) Unit tests are here to test if the page is respondant and if the model returns a good value for one of the top 5 Positive sentiment word: "Great"
