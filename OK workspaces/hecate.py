
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Hecate:
    def __init__(self, name="Hecate", personality="mysterious"):
        self.name = name
        self.personality = personality

    def respond(self, prompt):
        messages = [
            {"role": "system", "content": f"You are {self.name}, a daemon with a {self.personality} personality. Speak mythically."},
            {"role": "user", "content": prompt}
        ]
        completion = openai.ChatCompletion.create(model=os.getenv("OPENAI_MODEL", "gpt-4o"), messages=messages)
        return completion.choices[0].message.content
