import os
from google import genai

def get_gemini_response(prompt):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        return "Gemini API key is not configured. Please add it to your .env file."
    
    try:
        client = genai.Client(api_key=api_key)
        
        system_instruction = (
            "You are a calm, empathetic mental health support assistant. "
            "You are non-judgmental, supportive, and avoid giving medical diagnoses. "
            "Your tone should be light, soft, calming, and premium. Help the user feel better or just listen."
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
