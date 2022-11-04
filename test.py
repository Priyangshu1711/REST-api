import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes':10, 'name':'priyangshu' , 'views':10000},
        {'likes':11, 'name':'angshu' , 'views':103530},
        {'likes':12, 'name':'p' , 'views':10354584},
        {'likes':13, 'name':'pr' , 'views':135458},
        {'likes':14, 'name':'pri' , 'views':125234},
        {'likes':15, 'name':'priy' , 'views':13535},
        {'likes':16, 'name':'priya' , 'views':123456},
        {'likes':17, 'name':'priyan' , 'views':14554},
        {'likes':18, 'name':'priyang' , 'views':125533},
        {'likes':19, 'name':'priyangs' , 'views':15254},
        {'likes':20, 'name':'priyangsh' , 'views':224354},
        {'likes':21, 'name':'priyangshu' , 'views':56456},
        {'likes':22, 'name':'angs' , 'views':20000},
        {'likes':23, 'name':'ang' , 'views':30000},
        {'likes':24, 'name':'angsh' , 'views':40000},
        {'likes':25, 'name':'ngshu' , 'views':50000}]

'''for i in range (len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())

input()
'''
response = requests.get(BASE + "video/6")
print(response.json())
