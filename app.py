from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://api.tvmaze.com/schedule"
    response = requests.get(url)
    data = response.json()

    html = """
    <html>
    <head>
        <title>UniEvent</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f6f8;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #2c3e50;
            }
              .card {
                background: white;
                padding: 15px;
                margin: 10px auto;
                width: 60%;
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <h1>University Events</h1>
    """

    for event in data[:5]:
        name = event["name"]
        date = event["airdate"]

        html += f"""
        <div class="card">
            <h3>{name}</h3>
            <p><b>Date:</b> {date}</p>
        </div>
        """
      
    html += "</body></html>"

    return html

app.run(host="0.0.0.0", port=5000)
