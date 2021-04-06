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
    
    # path = "htmls"
    # directory=path+"/"+search
    # files = os.listdir(directory)
    # for filename in files:
    #     if os.path.isfile(directory+"/"+filename):
    #         f = open(filename, 'r', encoding="utf-8")
    #         lines = f.readlines()
    #         length = len(lines)
    #         i = 0
    #         description = "abstract"
    #         keywords="key1 key2"
    #         origin = "localhost:8000"+"/"+"static"+"/"+search+"/"+filename
    #         while i < length:
    #             dictt = {
    #                 "title": lines[i][:-1],
    #                 "description": description,
    #                 "keywords":keywords,
    #                 "origin": origin
    #             }
    #     dataNews.append(dictt)
        # print("kl",l)
        # i += 2


    path = "htmls"

    directory = path+"/"+str(search) #打开关键字对应目录
    files = os.listdir(directory)#列出该目录下所有文件名
    for filename in files:
        if os.path.isfile(directory+"/"+filename):
            print(filename)
            length=len(filename)
            # title=filename[:length-6]
            title = filename
            description="abstract"
            keywords="key1 key2"
            # origin="localhost:8000"+"/"+"static"+"/"+search+"/"+filename
            origin = "http://127.0.0.1:8000/static/"+ filename
            dictt={
                "title":title,
                "description":description,
                "keywords":keywords,
                "origin":origin
            }
            dataNews.append(dictt)
    print("directory"+directory)
    
    # print(dataNews[1]["title"])
    print(dataNews)


    return dataNews

# search="神舟五号"
# print(getlist(search,"hhh"))