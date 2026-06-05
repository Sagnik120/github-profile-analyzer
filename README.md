# GitHub Profile Analyzer

A Flask-based web application that analyzes GitHub profiles and provides useful insights such as repository statistics, language usage, top repositories, follower information, and more.

## Overview

GitHub Profile Analyzer allows users to enter any GitHub username and instantly view detailed information about that profile. The application fetches real-time data using the GitHub REST API and presents it in a clean and user-friendly interface.

This project demonstrates the use of API integration, backend development with Flask, data processing, and visualization using Matplotlib.

---

## Features

### Profile Information

* GitHub avatar
* Name and username
* Bio
* Profile URL
* Account creation date

### Repository Analytics

* Total public repositories
* Total stars received across repositories
* Most used programming language

### Top Repositories

* Displays the top 5 repositories based on star count
* Direct links to repositories

### Social Statistics

* Followers count
* Following count

### Language Analysis

* Automatic language detection from repositories
* Pie chart visualization of language distribution

### Real-Time Data

* Fetches live information directly from the GitHub API
* No database required

---

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS

### Libraries

* Requests
* Matplotlib

### API

* GitHub REST API

---

## Project Structure

```text
github-profile-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── language_chart.png
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Sagnik120/github-profile-analyzer.git
cd github-profile-analyzer
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How It Works

1. User enters a GitHub username.
2. Flask receives the request.
3. GitHub REST API is called.
4. Repository information is collected.
5. Statistics are calculated:

   * Total stars
   * Most used language
   * Top repositories
6. A language usage chart is generated.
7. Results are displayed on the dashboard.

---

## Example Insights

The analyzer can provide:

* Number of repositories
* Most active programming language
* Popular repositories
* Community reach through followers
* Language distribution across projects

---

## Learning Outcomes

This project helped in understanding:

* REST API integration
* JSON data processing
* Flask routing
* Template rendering with Jinja2
* Data visualization with Matplotlib
* Git and GitHub workflow
* Project structuring for deployment

---

## Future Improvements

* Interactive charts using Chart.js
* GitHub contribution analysis
* Repository growth tracking
* Repository filtering
* Export reports as PDF
* Dark mode support
* User authentication
* GitHub GraphQL API integration

---

## Author

**Sagnik Chandra**

B.Tech Graduate | AI & Machine Learning Enthusiast

GitHub: https://github.com/Sagnik120

---

## License

This project is open-source and available under the MIT License.
