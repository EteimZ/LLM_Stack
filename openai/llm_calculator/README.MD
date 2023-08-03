# LLM Calculator 

An LLM ehanced with a calculator using openai [functions](https://openai.com/blog/function-calling-and-other-api-updates).

## Usage

```bash
pip install openai
export OPENAI_API_KEY=XXXXXXYYYYYYZZZZZ
python main.py
```

This will launch a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) session with the LLM.

```bash
Human: What is the sine of 10
AI: The sine of 10 is approximately -0.5440211108893698.
Human: What is eight multiplied by ELeven
AI: Eight multiplied by eleven is equal to 88.
Human:
```

## Available functions

The LLM has access to the following mathematical functions.
- `eval`: This is the python [eval](https://docs.python.org/3/library/functions.html#eval) function. It is used to evaluate mathematical expressions. E.g: `eval('2+2')` gets evaluated to 4.
- `sin`: This function is used to get the sine of a number.
- `cos`: This function is used to get the cosine of a number.
- `tan`: This function is used to get the tangent of a number.
- `sqrt`: This function is used to get the square root of a number.
- `pow`: This is the python [pow](https://docs.python.org/3/library/functions.html#pow) function. It is used to perform exponention.
