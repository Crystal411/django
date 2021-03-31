import os
def getlist(search,result):

    dataNews = [{
            "title": search,
            "description": result,
            # "author": "张三",
            # "journal": "共搜索到"+str(len(result))+"个答案",
            "origin": "google"
            },
            ]
    

    path = "MilitaryShow/static"

    directory = path+"/"+str(search) #打开关键字对应目录
    files = os.listdir(directory)#列出该目录下所有文件名
    for filename in files:
        print(filename)
        length=len(filename)
        title=filename[:length-6]
        description="abstract"
        keywords="key1 key2"
        origin="localhost:8000"+"/"+"static"+"/"+search+"/"+filename
        dictt={
            "title":title,
            "description":description,
            "keywords":keywords,
            "origin":origin
        }
        dataNews.append(dictt)
    # print(directory)
    
    # print(dataNews[1]["title"])
    return dataNews

# search="神舟五号"
# print(getlist(search,"hhh"))