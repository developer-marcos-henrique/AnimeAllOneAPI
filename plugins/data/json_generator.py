import json



dict_objects = []

dict_objects.append(
    {
        "name": "anime",
        "sites": {
            "crunch": "xth.com",
            "night": "xtyt.com"
        }
    }
)


json_struct = {
    "series": [x for x in dict_objects]
}

print(json_struct)