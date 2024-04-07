import openai
import json
import math

# Functions that will be used by the llm
functions = [
    {
        "name": "eval",
        "description": "Useful for getting the result of a math expression. Input is a string of a math expression, output is the result of the expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The expression to be evalutated"
                }
            
            },
            "required": ["expression"],
        },
    },

    {
        "name": "sin",
        "description": "Useful for getting the sine of a number",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "number",
                    "description": "The number who's sine is to be calculated"
                }

            },
            "required": ["number"],
        },
    },

    {
        "name": "cos",
        "description": "Useful for getting the cosine of a number",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "number",
                    "description": "The number who's cosine is to be calculated"
                }

            },
            "required": ["number"],
        },
    },

    {
        "name": "tan",
        "description": "Useful for getting the tangent of a number",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "number",
                    "description": "The number who's tangent is to be calculated"
                }

            },
            "required": ["number"],
        },
    },

    {
        "name": "sqrt",
        "description": "Useful for getting the Square root of a number",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "number",
                    "description": "The number who's square root is to be calculated"
                }

            },
            "required": ["number"],
        },
    },

    {
        "name": "pow",
        "description": "Useful for performing exponentiation",
        "parameters": {
            "type": "object",
            "properties": {
                "base": {
                    "type": "number",
                    "description": "This the base number in exponentiation operation"
                },
                "exponent": {
                    "type": "number",
                    "description": "This the exponent number in exponentiation operation"
                },
            },
            "required": ["base", "exponent"],
        },
    }

]

def evaluate_function_call(function_name, arguments):
    """
    This functions handles the mapping of the llm functions to their actual implementation
    """

    function_map = {
        "eval": lambda args: eval(args["expression"]),
        "sin": lambda args: math.sin(args["number"]),
        "cos": lambda args: math.cos(args["number"]),
        "tan": lambda args: math.tan(args["number"]),
        "sqrt": lambda args: math.sqrt(args["number"]),
        "pow": lambda args: pow(args["base"], args["exponent"])
    }

    if function_name in function_map:
        return function_map[function_name](arguments)
    else:
        raise ValueError(f"Function '{function_name}' is not supported")

# memory of the LLM
msgs = []

while (prompt := input("Human: ")) != "exit":
    
    # Append user user's prompt to memory
    msgs.append({"role": "user", "content": prompt})
    
    # Send the user's prompt and functions to openai
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msgs,
        functions=functions,
        function_call="auto",
    )

    #get the response
    response_message = completion["choices"][0]["message"]

    # Check if the llm used a function
    if "function_call" in response_message:
        # Grab the function the llm called and the arguments it provided
        function_call = response_message["function_call"]
        function_name = function_call["name"]
        function_args = json.loads(function_call["arguments"])
        
        # call the function and get the response
        function_response = evaluate_function_call(function_name, function_args)
        
        # Append the LLM's response to memory
        msgs.append(response_message)
        
        # Append the function the LLM called and the response to memory
        msgs.append(
            {
                "role": "function",
                "name": function_name,
                "content": str(function_response),
            }
        )
        
        # Send the function and it's result to the LLM
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msgs,
            functions=functions,
            function_call="auto",
        )

    print("AI:", completion.choices[0].message["content"])
    msgs.append(response_message)

