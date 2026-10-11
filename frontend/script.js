//JAVASCRIPT 

const quizForm = document.getElementById("quizForm");
const resultSection = document.getElementById("result");
const scoreText = document.getElementById("score");
const recommendationText = document.getElementById("recommendation");

quizForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const studentName = document.getElementById("studentName").value.trim();

    const answers = {
        q1: document.getElementById("q1").value,
        q2: document.getElementById("q2").value,
        q3: document.getElementById("q3").value,
        q4: document.getElementById("q4").value,
        q5: document.getElementById("q5").value
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/api/quiz", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                student_name: studentName,
                topic: "Python Recursion",
                answers: answers
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not analyze quiz.");
        }

        scoreText.textContent =
            `Your score: ${data.score}/${data.total} (${data.percentage}%)`;

        recommendationText.textContent = data.recommendation;

        resultSection.hidden = false;
        resultSection.scrollIntoView({ behavior: "smooth" });

    } catch (error) {
        alert(
            "Unable to connect to the backend. Start the Flask server first."
        );
        console.error(error);
    }
});

document.getElementById("retryButton").addEventListener("click", function () {
    quizForm.reset();
    resultSection.hidden = true;
    quizForm.scrollIntoView({ behavior: "smooth" });
});
