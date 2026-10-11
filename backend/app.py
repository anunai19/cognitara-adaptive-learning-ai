
from flask import Flask, request, jsonify
from flask_cors import CORS

from database import initialize_database, save_attempt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ai"))
from recommend import recommend_intervention

app = Flask(__name__)
CORS(app)

CORRECT_ANSWERS = {
    "q1": "a",
    "q2": "b",
    "q3": "c",
    "q4": "a",
    "q5": "b"
}


@app.get("/")
def home():
    return jsonify({"message": "COGNITARA API is running"})


@app.post("/api/quiz")
def submit_quiz():
    data = request.get_json(silent=True) or {}

    name = data.get("student_name", "").strip()
    topic = data.get("topic", "")
    answers = data.get("answers")

    if not name or len(name) > 100:
        return jsonify({"error": "Enter a valid student name."}), 400

    if topic != "Python Recursion" or not isinstance(answers, dict):
        return jsonify({"error": "Invalid quiz submission."}), 400

    if set(answers.keys()) != set(CORRECT_ANSWERS.keys()):
        return jsonify({"error": "Please answer all five questions."}), 400

    if any(value not in ("a", "b", "c") for value in answers.values()):
        return jsonify({"error": "Invalid answer option."}), 400

    score = sum(
        answers[key] == correct
        for key, correct in CORRECT_ANSWERS.items()
    )

    total = len(CORRECT_ANSWERS)
    percentage = round((score / total) * 100)
    recommendation = recommend_intervention(percentage)

    save_attempt(
        name, topic, score, total, percentage, recommendation
    )

    return jsonify({
        "score": score,
        "total": total,
        "percentage": percentage,
        "recommendation": recommendation
    })


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
  
