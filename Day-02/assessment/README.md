# 🧑‍💻 User Introduction Generator – Python Beginner Task

This simple Python project is designed to help you practice **string manipulation**, **user input**, and **string formatting using `.format()`**.

---

## 📚 What You’ll Learn

- Working with user input
- Using string methods like `.title()`, `.lower()`, and `len()`
- Using `.format()` with indexing
- Detecting substrings using `in`
- Combining string operations into a meaningful output

---

## 📝 Task Description

Create a Python program that:

1. **Takes input** from the user:
   - Name
   - Age
   - City

2. **Performs string operations**:
   - Converts the name to **title case**
   - Converts the city name to **lowercase**
   - Converts the age to an **integer**

3. **Prints a formatted introduction** using `.format()` with **indexing**:
   ```
   Hello, my name is Raj. I'm 25 years old and I live in chandigarh.
   ```

4. **Displays the length** of the user's name:
   ```
   Length of your name: 3
   ```

5. **BONUS**: If `"raj"` (in any case) is found in the name, show:
   ```
   "raj" is found in the name!
   ```

---

## ✅ Sample Output

```python
# Sample Input:
# Name: raj
# Age: 25
# City: Chandigarh

# Sample Output:
Hello, my name is Raj. I'm 25 years old and I live in chandigarh.
Length of your name: 3
"raj" is found in the name!
```

---

## 🚀 How to Run

1. Save your Python code in a file called `intro_generator.py`
2. Run the file:

```bash
python intro_generator.py
```

---

## 🧠 Hints

- Use `input()` to get user input.
- Use `.title()` to capitalize names.
- Use `.lower()` to standardize city names.
- Use `.format()` with indexing like `{0}`, `{1}`, etc.
- Use `if "raj" in name.lower()` to check for substring match.

---

## 💡 Want a Challenge?

Try rewriting the output using **f-strings** after you complete the `.format()` version!

---

Happy coding! 🚀
