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
def sol(coeffs=[2.5, 1.3, -0.5]):
    a, b, c = coeffs
    discriminant = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + discriminant) / (2 * a)
```

## (optional) Your edited solution

Note: you may skip this section if AI-generated solution is correct.

No errors found — Gemini's solution was correct (ran and returned `True`), so this section is skipped.

## Screenshots of interaction with AI

![Gemini interaction for Problem 5](image-4.png)
