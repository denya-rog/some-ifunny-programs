from pprint import pprint

def update(data, service, count):
    pass


def main():
    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    print("Configuration before:")
    pprint(example_data)

    update(example_data, 'pylons', 7)

    print("Configuration after:")
    pprint(example_data)

if __name__ == '__main__':
    main()
    
    
    
a = {'abc':{"a":1,"b":2, "c":1}, "deh":{"d":1,"e":3, "h":1}}
service = "sdf"
count = 7
while count != 0:
    
    k = a.items()
    print(a.items())

    li= []
    for i in k:
        li.append(sum(i[1].values())) 
   
#    print(li)
    ind = li.index(min(li))
#    print(ind)
#    print(k[ind][0])
    name_serv = k[ind][0]
    dic_to_add = a[name_serv]
#    print(dic_to_add )
    if service in dic_to_add:
        dic_to_add[service] += 1
    else:
        dic_to_add[service] = 1
    count -= 1

###############################################################################

