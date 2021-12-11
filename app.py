from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.eva.pingutil.com/email?email=test@mail7.io" # 1. Insert API request URL

@app.route('/')
def index():
    # 2. Some APIs need a payload or extra data in the fields, set them up here:
    payload = {"email_address": "test@mail7.io",
        "domain": "mail7.io",
        "valid_syntax": true,
        "disposable": true,
        "webmail": false,
        "deliverable": true,
        "catch_all": true,
        "gibberish": false,
        "spam": false}
    
    # 3. Get the API Response in JSON
    api_response = requests.get(https://api.eva.pingutil.com/email?email=test@mail7.io, params=payload).json()
    
    # 4. Extract the information for the template
    title = api_response["Verify the email instantly"]
    image_url = api_response["https://api.eva.pingutil.com/email?email=test@mail7.io"]

    # 5. Return the Template with your data
    return render_template("index.html", title=title, image_url=image_url)

if __name__ == '__main__':
    app.run()
