from flask import Flask
from flask.templating import render_template
from controllers.transaction_controller import transactions_blueprint

app = Flask(__name__)

app.register_blueprint(transactions_blueprint)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)