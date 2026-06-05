from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return "User not found"

    user = response.json()

    repos_url = user["repos_url"]
    repos = requests.get(repos_url).json()

    total_stars = 0
    languages = {}

    for repo in repos:
        total_stars += repo["stargazers_count"]

        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    most_used = max(languages, key=languages.get) if languages else "N/A"

    data = {
        "name": user.get("name"),
        "username": user.get("login"),
        "followers": user.get("followers"),
        "following": user.get("following"),
        "public_repos": user.get("public_repos"),
        "stars": total_stars,
        "language": most_used,
        "avatar": user.get("avatar_url")
    }

    return render_template("result.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)