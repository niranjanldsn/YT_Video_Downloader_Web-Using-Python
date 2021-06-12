from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from main import download_video

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
     return render_template('index.html')

@app.route("/main", methods=['POST'])
def download():
    video1_url =request.form['firstvideo']
    download_video(video1_url)
    return render_template('index.html')

if __name__=='__main__':
    app.run(port=5000,debug=True)
