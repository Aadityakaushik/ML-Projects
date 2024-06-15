import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open("D:\jupyter/Source files/deployement/trained_breast_cancer_model.sav", 'rb'))



input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
prediction = loaded_model.predict(input_data)

if(prediction == 1):
    print("Breast cancer is Benign")
else:
    print("Breast cancer is  Malignant")

