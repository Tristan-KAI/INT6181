# Problem 1

## Your prompt to generate solution

```plain
AI model: Gemini

Write a Python function `sol()` (no parameters) for this exercise.

Goal: "Find a list of one hundred integers between 0 and 999 which all differ by at least ten from one another."

Your answer will be checked by this function (do NOT modify it):

def sat(li):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

Return only the body of `sol()`, i.e. a list of exactly 100 distinct integers (0..999) where every pair differs by at least 10.
```

## Initial AI-generated solution

```python
def sol():
    return list(range(0, 1000, 10))
```

## (optional) Your edited solution

Note: you may skip this section if AI-generated solution is correct.

No errors found — Gemini's solution is correct (ran and returned `True`), so this section is skipped.

## Screenshots of interaction with AI

Please capture the screenshot and paste it here.
