import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (5,166,72,19,175,25.8,0.587,51,3,2,1,5,1,5,2,5,11,5,3,5,1,5,2,3,5,2,5,2,5)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The transaction is fraud')
else:
  print('The transaction is not fraud')