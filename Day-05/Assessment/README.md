# Day 5 Assessment – Command Line Arguments & Environment Variables

## 1. Command Line Arguments

### Task 1: Basic Calculator

Write a Python script that accepts **two numbers** and an \**operator (+, -, *, /)** from the command line, then prints the result.

**Example run:**

```bash
python calc.py 10 5 +
```

**Output:**

```
Result: 15
```

---

### Task 2: Greeting Script

Write a script that accepts a **name** as a command line argument and prints:

```
Hello, <name>! Welcome to Python for DevOps.
```

---

## 2. Environment Variables

### Task 3: City Printer

* Set an environment variable `MY_CITY` with the name of your city.
* Write a Python script that reads the variable and prints:

```
You are coding from <MY_CITY>
```

---

### Task 4: Secret Manager Simulation

* Store a fake password in an environment variable `DB_PASSWORD`.
* Write a script that checks if `DB_PASSWORD` exists.

  * If it exists → print `Password retrieved successfully`
  * If not → print `Password not found`

---

## 3. Combined Task

### Task 5: CLI Config Tool

Write a Python script that:

1. Accepts a filename as a **command line argument**
2. Reads an environment variable `APP_MODE` (example: `dev`, `prod`)
3. Prints:

```
Running <filename> in <APP_MODE> mode
```

**Example run:**

```bash
setx APP_MODE "dev"   # Windows
python tool.py config.yaml
```

**Output:**

```
Running config.yaml in dev mode
```

---

✅ By completing these tasks, you’ll gain practical experience with **sys.argv** and **os.getenv**, two core concepts in building DevOps automation scripts.