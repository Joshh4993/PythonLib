# Python Life Simulation - **Project Brief**

## Pre-Reqs *(pip install)*:
>python-dotenv<br />
>pymongo<br />
>pyfiglet<br />

## Main Functions:
- Simulate a person
- Simulate a banking system
- Simulate a store
- Simulate a vending machine
- Simulate a social network
- Simulate God (Admin console)

## Person:
 - Define the _**Human** class:
 ```json
 {
    "obj_id": [mongoId],
    "first_name": String,
    "married_name": String,
    "maiden_name": String,
    "gender": String,
    "job": [Job],
    "relationships" : Array of [Relationships],
    "security_number": String,
    "bank_account": [Bank_Acc_mongoId],
    "wallet": Integer
 }
 ```
 - Explain the functions:
```json
 {
    "obj_id": Database given objectID- Unique value,
    "first_name": Human's First Name,
    "married_name": Human's Last Name (if Female and married),
    "maiden_name": Human's Last name (if Male or not married),
    "gender": Human's Gender,
    "job": Human's Employment,
    "relationships" : Array of Human Relationships,
    "security_number": Unique 12 character code for each Human (password),
    "bank_account": Human's Bank Account,
    "wallet": Human's change in wallet
 }
 ```

## Utility Classes:
- Define the _**Relationship** class:
```json
 {
    "from_human": [mongoId],
    "to_human": [mongoId],
    "relationship": String
 }
 ```
 - Explain the functions:
 ```json
 {
    "from_human": Database given objectID of source Human,
    "to_human": Database given objectID of referenced Human,
    "relationship": Description of relationship,
    "relationship_index" : {
       //This is the from : This is the reciprocal
        "mother_daughter" : "daughter_mother",
        "mother_son" : "son_mother",
        "father_daughter" : "daughter_father",
        "father_son" : "son_father",
        "brother_sister" : "sister_brother",
        "brother_brother" : "brother_brother",
        "sister_sister" : "sister_sister",
        "married" : "married",
        "engaged" : "engaged",
        "divorced" : "divorced"
    }
 }
 ```