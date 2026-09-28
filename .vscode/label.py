import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.DataFrame({
    'Gender':['Male','Female','Female','Male',]
})
encoder=LabelEncoder()
data['Gender_Encoded']=encoder.fit_transform(data['Gender'])
print(data)
