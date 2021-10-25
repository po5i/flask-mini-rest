from flask import Flask

from api import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)


@app.route("/")
def index():
    return "This is my awesome landing page 🤞"


if __name__ == "__main__":
    app.run(debug=True)
