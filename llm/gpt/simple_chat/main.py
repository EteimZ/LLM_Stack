from openai import OpenAI

client = OpenAI()

msgs = []

while (prompt := input("Human: ")) != "exit":
    
    msgs.append({"role": "user", "content": prompt})
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs
    )

    ai_response = completion.choices[0].message.content
    print("AI:", ai_response)
    msgs.append({"role": "assistant", "content": ai_response})
    

