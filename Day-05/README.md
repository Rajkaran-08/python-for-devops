# Python Command Line Arguments & Environment Variables

## 1. Command Line Arguments

Command line arguments are values you pass to a Python script when running it from the terminal. They make scripts flexible and reusable without changing the code.

You can access command line arguments using the `sys` module.

**Example:**

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

Run this script from the terminal:

```bash
python my_script.py hello world
```

Output:

```
Script name: my_script.py
Arguments: ['hello', 'world']
```

Here:

* `sys.argv[0]` → the script name
* `sys.argv[1:]` → the arguments passed

---

## 2. Environment Variables

Environment variables are values stored in the system’s environment. They are often used to store **configuration**, **API keys**, and **secrets**.

You can access them in Python using the `os` module.

**Example:**

```python
import os

# Get an environment variable
username = os.getenv("USER", "default_user")
print("Current user:", username)
```

To set an environment variable (Linux/macOS):

```bash
export MY_CITY=Chandigarh
```

On Windows (PowerShell):

```powershell
setx MY_CITY "Chandigarh"
```

Then, in Python:

```python
import os
print("City:", os.getenv("MY_CITY"))
```

---

## 3. DevOps Relevance

* **Command line arguments** are widely used in automation scripts, CI/CD pipelines, and tools that need flexible inputs.
* **Environment variables** are essential for security (storing passwords, tokens) and for running applications across environments (dev, staging, prod) without changing code.