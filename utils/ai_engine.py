import os
from openai import OpenAI

def get_openai_response(prompt):
    # Ab hum OpenAI ki library use karenge lekin Groq ke server se baat karenge
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        return "Groq API key is not configured. Please add it to Render Environment Variables."
    
    try:
        # Base URL badalna zaroori hai taaki request Groq ke paas jaye
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        
        system_message = (
            "You are a calm, empathetic mental health support assistant. "
            "You are non-judgmental, supportive, and avoid giving medical diagnoses. "
            "Your tone should be light, soft, calming, and premium. Help the user feel better or just listen."
        )

        # Model ka naam Groq wala use karenge (Llama 3.1 8B best aur free hai)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
