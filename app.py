from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://apodapi.herokuapp.com/api/" # 1. Insert API request URL

@app.route('/')
def index():
    # 2. Some APIs need a payload or extra data in the fields, set them up here:
    payload = {}
    
    # 3. Get the API Response in JSON
    api_response = requests.get(API_URL, params=payload).json()
    
    # 4. Extract the information for the template
    title = api_response["title"]
    image_url = api_response["url"]

    # 5. Return the Template with your data
    return render_template("index.html", title=title, image_url=image_url)

if __name__ == '__main__':
    app.run()