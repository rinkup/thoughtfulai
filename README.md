# README: Package Sorting Script

This README provides instructions on how to execute the Python script that determines the appropriate stack for packages based on their dimensions and mass.

---

## Prerequisites

Before executing the script, ensure you have the following:

1. **Python 3.x** installed on your system.
   - You can download Python from [python.org](https://www.python.org/).

2. A terminal or command prompt to run the script.

3. The Python file (e.g., `thoughtfulai.py`) saved locally.

---

## File Description

The script contains three functions:

1. **`is_bulky(width, height, length)`**:
   - Checks if a package is bulky based on its volume or dimensions.

2. **`is_heavy(mass)`**:
   - Checks if a package is heavy based on its mass.

3. **`sort(width, height, length, mass)`**:
   - Determines whether a package belongs in the `STANDARD`, `SPECIAL`, or `REJECTED` stack based on its bulkiness and weight.

The script also includes example calls to the `sort` function to demonstrate its usage.

---

## How to Run the Script

Follow these steps to execute the script:

1. Save the code to a Python file, for example, `thoughtfulai.py`.

2. Open a terminal or command prompt and navigate to the directory where the file is saved.

3. Run the script using the following command:

   ```bash
   python thoughtfulai.py
   ```

4. The output will display the stack classification for the example packages.

5. Run the unit test

    ```bash
    python -m unittest test_thoughtfulai.py
    ```

---

## Example Output

Running the script will produce the following output based on the provided examples:

```
STANDARD
SPECIAL
SPECIAL
REJECTED
REJECTED
```

Each line corresponds to the result of one of the example calls to the `sort` function.

---

## Unit Test

Running the unit test by 
    ```bash
    python -m unittest test_thoughtfulai.py
    ```

Result to expect

    ```
    Ran 3 tests in 0.000s

    OK
    ```

---


## Modifying the Script

To test the script with different package dimensions and masses, update the `print` statements at the end of the script. For example:

```python
print(sort(120, 80, 70, 15))  # Example custom input
```