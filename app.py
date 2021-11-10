from flask import Flask
from flask_cors import CORS

from api import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
CORS(app)


@app.route("/")
def index():
    """
    Index page
    """
    return "This is my awesome landing page 🤞"


if __name__ == "__main__":
    app.run(debug=True)
