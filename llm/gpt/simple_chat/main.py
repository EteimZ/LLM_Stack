import openai

msgs = []

while (prompt := input("Human: ")) != "exit":
    
    msgs.append({"role": "user", "content": prompt})
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msgs
    )
    
    print("AI:", completion.choices[0].message["content"])
    msgs.append(completion.choices[0].message)

