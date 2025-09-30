import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(data):
    prompt = f"Analyze this data: {data}. Provide a summary and 2-3 recommendations."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content
    parts = content.split("Recommendations:")
    return {
        "summary": parts[0].strip(),
        "recommendations": parts[1].strip()
    }