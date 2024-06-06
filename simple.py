from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-script')
def run_script():
    # Run the Selenium script
    process = subprocess.Popen(["python", "selenium_script.py"], stdout=subprocess.PIPE)
    process.wait()

    # Fetch the latest result from MongoDB
    client = MongoClient("mongodb://localhost:27017")
    db = client['twitter_trends']
    collection = db['trends']
    latest_result = collection.find().sort("datetime", -1).limit(1)

    return jsonify(latest_result)


if __name__ == '__main__':
    app.run(debug=True)
