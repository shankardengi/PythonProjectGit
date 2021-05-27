import json
if __name__ == "__main__":
    file = open("C:\\Users\\shankar.dengi\\Desktop\\json\\sample.json",'r')
    json = json.loads(file.read())
    list_keys = [i for i in json['elements'][0]]
    list_data = []
    for keys in list_keys:
        lists = [data[keys] for data in json['elements']]
        list_data.append((keys,lists))
    list_result = []
    for (key,value) in list_data:
        if len([value for i in value if isinstance(i,int)])>0:
            list_result.append((key,sum(value)))
            print(key,value)
        else:
            list_result.append((key, value))
    print("---------------------final aggeragation ----------------------------------")
    for i in list_result:
        print(i)



