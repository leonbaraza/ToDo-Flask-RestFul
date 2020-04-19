# TODO REGISTRY SERVICE

## Usage

All Responses will have the form

```
json
{
    "data":"Mixed type holding the content of the Response"
}
```

Subsequent response will only detail the expected value of the `data field`

### List all Todos

**Definition**

`GET /todos`

**Response**

- `200 OK` on success

``` json
[
    {
    "todoid":{"task":"Task comes here"}
    },
    {
        "todoid":{"task":"Task comes here"}
    }
]
```


### Register a new ToDo

**Definition**

`POST /todos`

**Arguments**
-`"Identifier" : string` its api generated you dont need to specify
-`"todo": String` a description of the todo

If the todo item already exists it will be overwritten

**Response**

- `201 OK` created

``` json
    {
    "todoid":{"task":"Task comes here"}
    }
```

### Look a ToDo details

**Definition**

`GET /todos/<identifier>`

**Response**

- `404 Not Found`If todo not found
- `200 OK` Success

``` json
    {
    "todoid":{"task":"Task comes here"}
    }
```

### DELETE a ToDo details

**Definition**

`DELETE /todos/<identifier>`

**Response**

- `404 Not Found`If todo not found
- `200 OK` Success
