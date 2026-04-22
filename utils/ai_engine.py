import os
from openai import OpenAI

def get_openai_response(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        return "OpenAI API key is not configured. Please add it to your .env file."
    
    try:
        client = OpenAI(api_key=api_key)
        
        system_message = (
            "You are a calm, empathetic mental health support assistant. "
            "You are non-judgmental, supportive, and avoid giving medical diagnoses. "
            "Your tone should be light, soft, calming, and premium. Help the user feel better or just listen."
        )

        response = client.chat.completions.create(
            model='gpt-4-mini',
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
