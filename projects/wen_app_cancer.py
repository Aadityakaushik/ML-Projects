import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("D:\jupyter/Source files/deployement/trained_breast_cancer_model.sav", 'rb'))

def cancer_pred(input_data):
    input_data_as_numpy = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)

    if(prediction[0] == 1):
        return "the cancer is Benign"
    else:
        return " the cancer is Malignant"

  
    
  
def main():
    
    
    # giving a title
    st.title('breast cancer Prediction Web App')
    
    
    # getting the input data from the user
    
    
    radius_mean = st.text_input('radius mean')
    texture_mean = st.text_input('texture mean')
    perimeter_mean = st.text_input('perimeter mean')
    area_mean = st.text_input('area mean')
    smoothness_mean = st.text_input('smoothness_mean')
    compactness_mean = st.text_input('compactness_mean')
    concavity_mean = st.text_input('concavity_mean')
    concave_points_mean  = st.text_input('concave points mean ')
    symmetry_mean  = st.text_input('symmetry_mean ')
    fractal_dimension_mean = st.text_input('fractal_dimension_mean')
    radius_se = st.text_input('radius_se ')
    texture_se  =  st.text_input('texture_se')   
    perimeter_se = st.text_input('perimeter_se') 
    area_se      = st.text_input('area_se')
    smoothness_se  = st.text_input('smoothness_se ')
    compactness_se   = st.text_input('compactness_se ')
    concavity_se=st.text_input('concavity_se')
    concave_points_se =st.text_input('concave points_se ')
    symmetry_se=st.text_input('symmetry_se')
    fractal_dimension_se=st.text_input('fractal_dimension_se')
    radius_worst=st.text_input('radius_worst')
    texture_worst=st.text_input('texture_worst')
    perimeter_worst=st.text_input('perimeter_worst')
    area_worst=st.text_input('area_worst')
    smoothness_worst=st.text_input('smoothness_worst')
    compactness_worst=st.text_input('compactness_worst')
    concavity_worst=st.text_input('concavity_worst')
    concave_points_worst=st.text_input('concave points_worst')
    symmetry_worst=st.text_input('symmetry_worst')
    fractal_dimension_worst=st.text_input('fractal_dimension_worst')
       
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('cancer Test Result'):
        diagnosis = cancer_pred([radius_mean,texture_mean, perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se ,compactness_se ,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])
        
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()