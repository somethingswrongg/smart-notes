async function summarize() {
    const text = document.getElementById("text").value;
    const resultBlock = document.getElementById("result");
    const resultContent = document.getElementById("result-content");

    resultBlock.style.display = "block";
    resultContent.innerText = "⏳ Обработка...";

    try {
        const response = await fetch("http://localhost:8000/api/ai/summarize/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNzQyNDUzLCJpYXQiOjE3NzE2NTYwNTMsImp0aSI6IjllZmE4MDZiZjc5MDRkNGZiMDUyY2IwNjVjZWI4MzBiIiwidXNlcl9pZCI6IjEifQ.PuVZ-hVIWJSQIPuENn6g9R3DuZ47uj68uH1AgivE1iA"}`
            },
            body: JSON.stringify({ text }),
        });

        if (!response.ok) {
            throw new Error("Ошибка сервера");
        }

        const data = await response.json();

        resultContent.innerText =
            data ||
            "❌ Пустой ответ от сервера";


    } catch (err) {
        resultContent.innerText = "❌ Ошибка. Попробуйте позже.";
    }
}

