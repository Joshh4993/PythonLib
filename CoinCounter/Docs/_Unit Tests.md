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
        "accuracy": "100.00",
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
        "accuracy": "100.00",
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

 # Test Case #2

**Purposes:**
 - Check UI for register function

  **Attempts of registration (inital database does not have pre-existing users):**
  | Attempt # | Name | Username | Password | Confirm Password | Expected Result | Result |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1 | Josh Edwards | Joshh4993 | TestPW | TestPW | User Successfully registered, username to lowercase, dashboard loads | User Successfully registered, username to lowercase, dashboard loads |
| 2 | James Kilmer | Joshh4993 | TestPW | TestPW | Username taken, error message displayed | Username taken, error message displayed |
| 3 | James Kilmer | JamesK29 | TestPW | TestPW | User Successfully registered, username to lowercase, dashboard loads | User Successfully registered, username to lowercase, dashboard loads |
| 4 | James Kilmer | JamesK27 | TestPW | TestPW1 | Password Check Failed, display error message | Password Check Failed, display error message |
| 5 | Mary Clark | MaryK09 | TestPW | TestPW | User Successfully registered, username to lowercase, dashboard loads | User Successfully registered, username to lowercase, dashboard loads |
| 6 | Billy Joel | BillyJ219 | TestPW | TestPW | User Limit Reached, No account made, error code "ERROR_ACCS" displayed | User Limit Reached, No account made, error code "ERROR_ACCS" displayed |


**Comments**
 > Works as intended. No action to be taken.

 ---