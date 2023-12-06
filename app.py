import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model_tree_model.sav', 'rb'))


# creating a function for Prediction

def fraudulent_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The transaction is not fraud.'
    else:
      return 'The transaction is fraud.'
  
    
  
def main():
    
    
    # giving a title
    st.title('Credit Card Fraud Prediction Web Integration')
    
    
    # getting the input data from the user
    
    
    V1 = st.text_input('Enter value for V1')
    V2 = st.text_input('Enter value for V2')
    V3 = st.text_input('Enter value for V3')
    V4 = st.text_input('Enter value for V4')
    V5 = st.text_input('Enter value for V5')
    V6 = st.text_input('Enter value for V6')
    V7 = st.text_input('Enter value for V7')
    V8 = st.text_input('Enter value for V8')
    V9 = st.text_input('Enter value for V9')
    V10= st.text_input('Enter value for V10')
    V11= st.text_input('Enter value for V11')
    V12= st.text_input('Enter value for V12')
    V13= st.text_input('Enter value for V13')
    V14= st.text_input('Enter value for V14')
    V15= st.text_input('Enter value for V15')
    V16= st.text_input('Enter value for V16')
    V17= st.text_input('Enter value for V17')
    V18= st.text_input('Enter value for V18')
    V19= st.text_input('Enter value for V19')
    V20= st.text_input('Enter value for V20')
    V21= st.text_input('Enter value for V21')
    V22= st.text_input('Enter value for V22')
    V23= st.text_input('Enter value for V23')
    V24= st.text_input('Enter value for V24')
    V25= st.text_input('Enter value for V25')
    V26= st.text_input('Enter value for V26')
    V27= st.text_input('Enter value for V27')
    V28= st.text_input('Enter value for V28')
    Amount= st.text_input('Enter value for Amount(in USD)')
    
    # code for prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Prediction'):
        prediction = fraudulent_prediction([V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount])
        
        
    st.success(prediction)
    
    
    
    
if __name__== '__main__':
    main()