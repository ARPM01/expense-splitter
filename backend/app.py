from flask import Flask
from flask_cors import CORS

from config import Config
from models import init_db

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

CORS(
    app,
    resources={r"/*": {"origins": "*", "headers": "Content-Type"}},
)

init_db(app)

from routes.transactions import transactions_bp
from routes.users import users_bp

app.register_blueprint(transactions_bp, url_prefix="/api/transactions")
app.register_blueprint(users_bp, url_prefix="/api/users")


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
