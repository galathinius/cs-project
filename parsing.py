import re
import json


def parse(file_name):
    f1 = open(file_name, "r")
    file_read = f1.read().replace('\n', 'bred').replace('\r', 'bred')

    pattern = r'<custom_item>(.*?)</custom_item>'

    x = re.findall(pattern, file_read)
    x = [i.split('bred') for i in x]

    parsed_data = {}

    for i in range(0, len(x)):
        item = {}
        for j in x[i]:
            is_it = re.search(":", j)
            if is_it:
                j = j.replace('"', '')
                row = j.split(':')
                item[row[0].strip()] = row[1].strip()
        parsed_data[i] = item

    f2 = open('parsed.json', "w")
    f2.write(json.dumps(parsed_data))

    f1.close()
    f2.close()

    re.purge()

# parse("example.txt")
