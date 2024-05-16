# import flask, scikit-learn, pandas, pickle-mixin
import pandas as pd
from flask import Flask, render_template, request
import category_encoders as ce
import pickle

app = Flask(__name__)
data = pd.read_csv("cleaned_data.csv")
model = pickle.load(open("Best_Model.pkl", 'rb'))

@app.route('/')
def index():

    locations = sorted(data['City'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():

    city = request.form.get('location')
    beds = request.form.get('beds')
    baths = request.form.get('baths')
    province = request.form.get('province')

    print(city, beds, baths, province)
    #encode city and province before sending to the model.

    input = pd.DataFrame([[city,beds,baths,province]], columns = ['City', 'Number_Beds', 'Number_Baths', 'Province'])
    encoder = ce.BinaryEncoder()
    input['City'] = encoder.fit_transform(input['City'])
    input['Province'] = encoder.fit_transform(['Province'])
    prediction = model.predict(input)[0]

    return str(prediction)
if __name__=="__main__":
    app.run(debug=True, port=5001)