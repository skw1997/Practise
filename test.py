import math
import os
import time
from concurrent.futures import ThreadPoolExecutor
import uuid
# path = "第二层文件/"
# path = path.strip('/')
# sub = "test-bin-1-07G.zip".strip('/')
# x_id = 1
# print('/root/dataset/{}/{}/{}'.format(str(x_id), path, sub))
#
# visited = [[1,2,3,],[4,5,6]]
# for x in range(3):
#     for y in range(2):
#         print(visited[y][x])
from collections import defaultdict

from hdfs import InsecureClient
#
client = InsecureClient(url='http://192.168.100.202:9870', user='root')
#
# if not client.status(hdfs_path="/forkcloud/forkcloud-proxy/dataset/16/1/1/1", strict=False):
#     client.makedirs(hdfs_path="/forkcloud/forkcloud-proxy/dataset/16/1/1/1")
# filename = 'vgg16.png'
# # name, ext = os.path.splitext(filename)
# # filename = name + str(uuid.uuid4()) + ext
# x_id = 'test'
#
# url = 'http://{}:{}/{}/{}'.format('192.168.100.202', 30008, x_id, filename)
# print(url)
# st = time.time()
# with ThreadPoolExecutor() as executor:
#     for parent, dirnames, filenames in os.walk('C:/Users/Administrator/Desktop/temp'):
#         for file in filenames:
#             dir = parent+"/"+file
#             # client.upload('/forkcloud/forkcloud-proxy/dataset/143/', dir)
#             executor.submit(client.upload,'/forkcloud/forkcloud-proxy/dataset/t1/', dir)
#             # print(parent+file)
# ed = time.time()
# print(ed - st)

#
# print(20*math.log(8))
#
# st2 = time.time()
# with ThreadPoolExecutor(10) as executor:
#     for parent, dirnames, filenames in os.walk('C:/Users/Administrator/Desktop/bloodmnist'):
#         for file in filenames:
#             dir = parent+"/"+file
#             # client.upload('/forkcloud/forkcloud-proxy/dataset/143/', dir)
#             executor.submit(client.upload,'/forkcloud/forkcloud-proxy/dataset/t2/', dir)
#             # print(parent+file)
# ed2 = time.time()
# print(ed2 - st2)
#
# st3 = time.time()
# with ThreadPoolExecutor(10) as executor:
#     for parent, dirnames, filenames in os.walk('C:/Users/Administrator/Desktop/temp'):
#         for file in filenames:
#             dir = parent+"/"+file
#             # client.upload('/forkcloud/forkcloud-proxy/dataset/143/', dir)
#             executor.submit(client.upload,'/forkcloud/forkcloud-proxy/dataset/t3/', dir)
#             # print(parent+file)
# ed3 = time.time()
# print(ed3 - st3)

# str = "/forkcloud/forkcloud-proxy/dataset/1"
# fold = os.path.basename(str)
# print(str.rstrip(fold))

# ls = [{'name': 'abc' , 'x_id': 119},{'name': 'abcd' , 'x_id': 123},{'name': 'abcde' , 'x_id': 127},{'name': 'f' , 'x_id': 128},{'name': 'g' , 'x_id': 129},{'name': 'h' , 'x_id': 130}]
# result_list = []
# totalUsage = 0
# for result in ls:
#     usage = int(client.content('/forkcloud/forkcloud-proxy/dataset/{}'.format(result['x_id'])).get("length"))
#     totalUsage += usage
#     data = {
#         'name': result['name'],
#         'size': usage
#     }
#     result_list.append(data)
# result_list.sort(key=lambda k: (k.get('size'), 0), reverse=True)
# finalList = [{'Total': totalUsage}]
# for i in range(2):
#     result_list[i]['percent'] = round(float(result_list[i]['size']) * 100 / float(totalUsage), 2)
#     finalList.append(result_list[i])
#
# for i in range(len(finalList)):
#     print(finalList[i])
a = 3
b = 5
a = a^b
print(a)
b = a^b
print(b)
a = a^b
print(a)
