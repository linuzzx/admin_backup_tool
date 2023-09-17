# Admin-Backend-Tool for teachers

This is my attempt at an grade entry and management REST API. 

## data.json format

```json
{
    "Max": [ //student's name
        [
            "SA", // type of grade
            2 // value of grade
        ]
    ]
}
```
The weight of a grade is specified in grade_weights in admin_backup_tool.py

If a grade type isn't specified in this dictionary, the weight is 1


## Example requests

#### This will add the student "Max"
```
curl -H "Content-Type: application/json" --request POST http://127.0.0.1:5000/add_student -d "{\"name\":\"Max\"}"
```

#### This will add a grade of the type "SA" with the value 3 to "Max"
```
curl -H "Content-Type: application/json" --request POST http://127.0.0.1:5000/add_grade -d "{\"name\":\"Max\",\"grade_type\":\"SA\",\"grade\":3}"
```

#### This will return the grades of the student "Max"
```
curl -H "Content-Type: application/json" --request POST http://127.0.0.1:5000/get_student -d "{\"name\":\"Max\"}"
```

#### This will remove the grade of the type "SA" with the value 3 of "Max"
```
curl -H "Content-Type: application/json" --request POST http://127.0.0.1:5000/remove_grade -d "{\"name\":\"Max\",\"grade_type\":\"SA\",\"grade\":3}"

```

#### This will remove the student "Max"
```
curl -H "Content-Type: application/json" --request POST http://127.0.0.1:5000/remove_student -d "{\"name\":\"Max\"}"
```

#### This will return a json table with all students and their average grade, sorted best to worst
```
curl -H "Content-Type: application/json" --request GET http://127.0.0.1:5000/list_students
```


