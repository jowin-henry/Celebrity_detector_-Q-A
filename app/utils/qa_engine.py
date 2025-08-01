import os
import requests

class QAEngine:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        # self.model  = "meta-llama/llama-4-maverick-17b-128e-instruct"
        self.model = "meta-llama/llama-4-scout-17b-16e-instruct"

    def ask_about_celebrity(self,name,question):
        headers = {
            "Authorization" : f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        prompt = f"""
                    You are a helpful AI assistant specialized in celebrity knowledge. Provide concise, accurate, and respectful answers about {name}.
                    Question : {question}
                    """
        
        payload  = {
            "model" : self.model,
            "messages" : [{"role" : "user" , "content" : prompt}],
            "temperature" :  0.5,
            "max_tokens" : 512
        }

        response = requests.post(self.api_url , headers=headers , json=payload)

        if response.status_code==200:
            return response.json()['choices'][0]['message']['content']
        
        return "Sorry I couldn't find the answer"