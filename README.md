# Machine learning model on Flask <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">

This is a basic project which runs a machine learning model on the flask. 
Here, I have implemented an SVM classifier to predict the hear attack condition in the patient. 
The dataset is available on the archive folder. For more details about the dataset check out [Kaggle](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset "Heart Attack Analysis & Prediction Dataset").

## Model used for classification 
### SVM 
You can check that in the [heart_attack.ipynb](https://github.com/Arshad221b/Machine-Learning-with-flask/blob/master/heart_attack.ipynb)
Got accuracy of 82% with F1 score of 81.
Model weights are stored in finalized_model.sav

You can read my blog on SVM [here](https://www.arshad-kazi.com/mathematics-behind-svmsupport-vector-machine/).

## Flask Integration 
Created an front end page with html. The flask is used to run these pages. [model_prediction.py](https://github.com/Arshad221b/Machine-Learning-with-flask/blob/master/model_prediction.py) is where all the post requests are processed and prediction is made. 

## Screenshots
| Home      | Results      | 
|------------|-------------| 
<img src="https://github.com/Arshad221b/Machine-Learning-with-flask/blob/master/images/Screenshot%202021-06-17%20at%203.23.52%20PM.png"> |<img src="https://github.com/Arshad221b/Machine-Learning-with-flask/blob/master/images/Screenshot%202021-06-17%20at%203.09.41%20PM.png">

---
### Run app.py
---
