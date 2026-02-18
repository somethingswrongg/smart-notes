# для локальной модели LLama

# import httpx
#
# OLLAMA_URL = "http://localhost:11434/api/generate"
#
# async def summarize_text(text: str) -> str:
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         response = await client.post(
#             OLLAMA_URL,
#             json={
#                 "model": "llama3",
#                 "prompt": f"Summarize briefly:\n\n{text}",
#                 "stream": False
#             },
#         )
#
#     data = response.json()
#
#     if "response" not in data:
#         raise Exception(f"Ollama error: {data}")
#
#     return data["response"]


# OpenAI

# import os
# import httpx
# from dotenv import load_dotenv
#
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#
#
# async def summarize_text(text: str) -> str:
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             "https://api.openai.com/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {OPENAI_API_KEY}",
#                 "Content-Type": "application/json",
#             },
#             json={
#                 "model": "gpt-4o-mini",
#                 "messages": [
#                     {"role": "system", "content": "Summarize the text briefly."},
#                     {"role": "user", "content": text},
#                 ],
#             },
#         )
#
#     data = response.json()
#     print("STATUS:", response.status_code)
#     print("OPENAI RESPONSE:", data)
#
#     if "choices" not in data:
#         raise Exception(f"OpenAI error: {data}")
#
#     return data["choices"][0]["message"]["content"]


# HuggingFace

# import os
# import httpx
# from dotenv import load_dotenv
#
# load_dotenv()
#
# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_API_URL = "https://router.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
#
# async def summarize_text(text: str) -> str:
#     async with httpx.AsyncClient(timeout=60.0) as client:
#         response = await client.post(
#             HF_API_URL,
#             headers={
#                 "Authorization": f"Bearer {HF_API_KEY}",
#                 "Content-Type": "application/json",
#             },
#             json={
#                 "inputs": text,
#             },
#         )
#
#     data = response.json()
#
#     print("STATUS:", response.status_code)
#     print("HF RESPONSE:", data)
#
#     # HuggingFace возвращает список
#     if isinstance(data, list) and "summary_text" in data[0]:
#         return data[0]["summary_text"]
#
#     # Если ошибка
#     if "error" in data:
#         raise Exception(f"HuggingFace error: {data['error']}")
#
#     raise Exception(f"Unexpected response: {data}")
#
#
# Cohere
#
#
# import os
# import httpx
#
# # Берем ключ из переменных окружения
# COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# COHERE_API_URL = "https://api.cohere.ai/v1/summarize"  # endpoint для summarization
#
# async def summarize_text(text: str) -> str:
#     """
#     Отправляет текст на Cohere API и возвращает краткое summary.
#     """
#     headers = {
#         "Authorization": f"Bearer {COHERE_API_KEY}",
#         "Content-Type": "application/json",
#     }
#
#     payload = {
#         "text": text,
#         "length": "medium",  # короткий/medium/long
#         "format": "paragraph"  # можно "paragraph" или "bullet_points"
#     }
#
#     async with httpx.AsyncClient() as client:
#         response = await client.post(COHERE_API_URL, headers=headers, json=payload)
#
#         # Проверка ответа
#         if response.status_code != 200:
#             raise Exception(f"Cohere API error: {response.status_code} {response.text}")
#
#         data = response.json()
#         # В зависимости от версии API, summary может быть в data['summary'] или data['summaries'][0]
#         if "summary" in data:
#             return data["summary"]
#         elif "summaries" in data and len(data["summaries"]) > 0:
#             return data["summaries"][0]
#         else:
#             raise Exception(f"Cohere returned unexpected data: {data}")
