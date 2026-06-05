from flask import Flask, render_template, request
import requests
import os

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    username = request.form['username']

    user_url = f"https://api.github.com/users/{username}"

    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        return "GitHub User Not Found"

    user = user_response.json()

    repos = requests.get(
    f"{user['repos_url']}?per_page=100"
).json()

    total_stars = 0
    languages = {}
    repo_data = []

    for repo in repos:

        stars = repo["stargazers_count"]
        total_stars += stars

        repo_data.append({
            "name": repo["name"],
            "stars": stars,
            "url": repo["html_url"]
        })

        lang = repo["language"]

        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    # Top 5 repositories
    top_repos = sorted(
        repo_data,
        key=lambda x: x["stars"],
        reverse=True
    )[:5]

    # Most used language
    most_used = (
        max(languages, key=languages.get)
        if languages
        else "N/A"
    )

    # Generate language chart
    if languages:

        chart_path = os.path.join(
            app.static_folder,
            "language_chart.png"
        )

        plt.figure(figsize=(6, 6))

        plt.pie(
            languages.values(),
            labels=languages.keys(),
            autopct='%1.1f%%'
        )

        plt.title("Language Usage")

        plt.savefig(
            chart_path,
            bbox_inches="tight"
        )

        plt.close()

    data = {
        "name": user.get("name"),
        "username": user.get("login"),
        "bio": user.get("bio"),
        "avatar": user.get("avatar_url"),
        "followers": user.get("followers"),
        "following": user.get("following"),
        "public_repos": user.get("public_repos"),
        "stars": total_stars,
        "language": most_used,
        "created_at": user.get("created_at")[:10],
        "profile_url": user.get("html_url"),
        "top_repos": top_repos,
        "languages": languages
    }

    return render_template(
        "result.html",
        data=data
    )
if __name__ == "__main__":
    app.run(debug=True)