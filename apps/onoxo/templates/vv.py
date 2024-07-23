import json

data = '{"data": [{"name": "Үсөн","last_name": "Момунов","email": "uson.momunov@kstu.kg","Org Unit Path [Required]": "\/kstu.kg\/Student KSTU\/INIT\/IST-3-22"}, {"name": "Өмүрбек","last_name": "Шерматов","email": "o.shermatov@kstu.kg","Org Unit Path [Required]": "\/kstu.kg\/Dovuzovskia podrozdelenia\/Balykchinsky kolledzh"}]}'

parsed_data = json.loads(data)

sorted_data = sorted(parsed_data["data"], key=lambda x: x["name"])

for item in sorted_data:
    print(item["name"], item["email"])