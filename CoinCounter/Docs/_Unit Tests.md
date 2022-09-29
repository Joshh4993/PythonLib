# OpenCoin - Unit Tests

---

## Overview

This document outlines all tests ran on the system as it is developed.

---

# Test Case #1

**Purposes:**
 - To ensure the login functions work as intended
 - Check that databases load and save as intended

**Input Data:**
```python
 return_value, username = register_volunteer("username", "name", "TestPassword")
 print(f'Value: {return_value}\nUsername: {username}')
```

**Expected Result:**
 - *Database:*
    ```json
    {
        "username": {
        "accuracy": 10000,
        "bags_checked": 0,
        "bags_correct": 0,
        "last_session": "HAS NOT LOGGED IN",
        "name": "name",
        "password": "b'$2b$12$aSRBPsFdghmecc0cJVyule8CFtAQ.uSJNMGquJ264cVpHcez5I6pO'"
    }
    }
    ```
  - *Terminal Output:*
    > Value: True
    > Username: username

**Actual Result:**
 - *Database:*
    ```json
    {
        "username": {
        "accuracy": 10000,
        "bags_checked": 0,
        "bags_correct": 0,
        "last_session": "HAS NOT LOGGED IN",
        "name": "name",
        "password": "b'$2b$12$aSRBPsFdghmecc0cJVyule8CFtAQ.uSJNMGquJ264cVpHcez5I6pO'"
    }
    }
    ```
  - *Terminal Output:*
    > Value: True
    > Username: username

**Comments**
 > Works as intended. No action to be taken.

 ---