from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    sr = "/programmerhumor"
    url = "https://meme-api.com/gimme" + sr
    response = json.loads(requests.request("GET", url).text)
    
    meme_large = response["preview"][-2]   # Meme image URL
    subreddit = response["subreddit"]      # Subreddit name
    title = response["title"]              # Post title
    
    return meme_large, subreddit, title

@app.route("/")
def index():
    meme_pic, subreddit, title = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, title=title)

app.run(host="0.0.0.0", port=5000)