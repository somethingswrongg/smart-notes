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
                'Authorization': `Bearer ${"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNjAwODg2LCJpYXQiOjE3NzE1MTQ0ODYsImp0aSI6IjZjYmMwZmQ2NTJjMTRlNGE5N2E4MDcwMGY3NWFmNmZjIiwidXNlcl9pZCI6IjEifQ.dbwRDo6dfDVkMRlL2w7qkDKlr_Jcvr_lpMHIm-WlJAg"}`
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

