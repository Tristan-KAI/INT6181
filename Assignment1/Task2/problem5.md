# Problem 5

## Your prompt to generate solution

```plain
AI model: Gemini

Write a Python function `sol(coeffs=[2.5, 1.3, -0.5])` for this exercise.

Goal: "Find any (real) solution to a*x^2 + b*x + c = 0, where coeffs = [a, b, c]."

Your answer will be checked by this function (do NOT modify it):

def sat(x, coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    return abs(a * x ** 2 + b * x + c) < 1e-6

Return only the body of `sol()`. Solve it with the general quadratic formula (do NOT hardcode the specific answer).
```

## Initial AI-generated solution

```python
# AI-generated solution here
def sol(coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    discriminant = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + discriminant) / (2 * a)
```

## (optional) Your edited solution

Note: you may skip this section if AI-generated solution is correct.

The errors found in the AI-generated solution:
1. to be filled here
2. 
3.

Your edited solution:

```python
# your solution after debugging here
```

## Screenshots of interaction with AI

Please capture the screenshot and paste it here.
![alt text](image-4.png)