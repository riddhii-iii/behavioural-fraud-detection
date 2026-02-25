from flask import Flask, request, jsonify, render_template
from src.predict import predict_risk
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sessions.db"
db = SQLAlchemy(app)
class LoginSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    risk_score = db.Column(db.Float)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    risk_score = predict_risk(data)
    session = LoginSession(risk_score=risk_score)
    db.session.add(session)
    db.session.commit()

    return jsonify({
        "risk_score": risk_score,
        "prediction": "High Risk ⚠️" if risk_score > 0.7 else "Low Risk ✅"
    })

if __name__ == "__main__":
    app.run(debug=True)