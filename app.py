from flask import Flask
from routes.complaints_routes import complaint_bp
from routes.admin_routes import admin_bp
from database import init_db
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

init_db()

app.register_blueprint(admin_bp)
app.register_blueprint(complaint_bp)

if __name__ == "__main__":
    app.run(debug=True)
