from flask import Flask, render_template, request, jsonify  # type: ignore
from connect import db
from bs4 import BeautifulSoup  # type: ignore
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("movie.html")


@app.route("/create", methods=["POST"])
def create_movie():
    
    url_recieve = request.form["movieUrl"]
    star_receive = request.form["star"]
    comment_recieve = request.form["comment"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    data = requests.get(url_recieve, headers=headers)
    soup = BeautifulSoup(data.text, "html.parser")
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')
    image = og_image["content"]
    title = og_title["content"]
    description = og_description["content"]
    doc = {
        "title": title,
        "image": image,
        "description": description,
        "star": star_receive,
        "comment": comment_recieve,
    }
    print(doc)
    db.movies.insert_one(doc)
    return jsonify(
        {
            "result": "success",
            "msg": "Created",
        }
    )


@app.route('/movies',methods=['GET'])
def get_movies():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify(movie_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
