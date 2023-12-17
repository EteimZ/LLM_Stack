import os
import google.generativeai as genai


genai.configure(api_key=os.environ["GEMINI_KEY"])

model = genai.GenerativeModel(model_name="gemini-pro")

convo = model.start_chat(history=[])

while (prompt := input("Human: ")) != "exit":

    convo.send_message(prompt)

    print("AI:", convo.last.text)
