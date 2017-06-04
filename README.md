# Convert JSON object to Swagger schema definition YAML

The script reads input from stdin and prints the result to stdout.
Supports object, array, integer, float and string types.

Example usage
```
sh> cat file.json | python ssg.py
```

Example JSON
```
{
    "prop1": [
        "v1", "v2", "v3"
    ],
    "prop2": {
        "k1": 123,
        "k2": [4,5,6]
    }    
} 
```

Example output schema YAML
```
schema:
    type: object
    properties:
        prop1:
            type: array
            description: prop1
            items:
                type: string
                description: prop1 item
        prop2:
            type: object
            description: prop2
            properties:
                k2:
                    type: array
                    description: k2
                    items:
                        type: integer
                        description: k2 item
                k1:
                    type: integer
                    description: k1
```

