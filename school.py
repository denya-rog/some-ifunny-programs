from pprint import pprint

def update(data, service, count):
    while count != 0:
    
        k = data.items()
        print(data.items())

        li = []
        for i in k:
            li.append(sum(i[1].values())) 
   
#    print(li)
        ind = li.index(min(li))
        name_serv = k[ind][0]
        dic_to_add = data[name_serv]
#    print(dic_to_add )
        if service in dic_to_add:
            dic_to_add[service] += 1
        else:
            dic_to_add[service] = 1
        count -= 1
    return data


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
    

###############################################################################

