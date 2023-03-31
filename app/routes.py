from flask import render_template

@app.route("/")
def index():
    return render_template(landing.html)

@app.route("/dashboard")
def dashboard():
    return render_template(dashboard.html)