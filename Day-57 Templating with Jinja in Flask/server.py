from flask import Flask, render_template
import random
import requests
from datetime import date
app = Flask(__name__)

agify_endpoint = "https://api.agify.io?"
genderize_endpoint = "https://api.genderize.io?"


@app.route('/')
def home():
    current_year = date.today().year
    my_name = "Phuc Thai Le"
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year, MY_NAME=my_name)

@app.route('/guess/<string:name>')
def guess(name):
    parameter={
        "name": f"{name}",
    }
    age_response = requests.get(url=agify_endpoint, params=parameter)
    gender_response = requests.get(url=genderize_endpoint, params=parameter)

    age_data = age_response.json()
    gender_data = gender_response.json()

    age = age_data['age']
    gender = gender_data['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/97dfc4437979c5fdcaf3"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)