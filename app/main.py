from dotenv import load_dotenv
import os
from flask import Flask


# Load environment variables from .env
load_dotenv()

# Now can use environment variables
secret = os.getenv("SECRET_KEY")
print("Secret Key:", secret)  # Just for testing — remove in prod


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, DevOps World!"

@app.route("/secret")
def show_secret():
    return f"Secret is: {os.getenv('SECRET_KEY')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
