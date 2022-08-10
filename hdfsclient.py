# 连接hdfs服务
import datetime
import time

from flask import make_response
from hdfs import InsecureClient
import os

# tim = str(time.time())
# print(tim)
def get_chunk_filename(prefix, filename, chunk_number):
        chunk_filename = filename + '-' + str(chunk_number)
        if chunk_filename.startswith(prefix):
            return chunk_filename
        return '{}/{}'.format(prefix, chunk_filename)


client1 = InsecureClient('http://192.168.100.101:9870', user='root')
client2 = InsecureClient('http://192.168.100.101:9870', user='root')
# hdfs_path = '/forkcloud/forkcloud-proxy/dataset/111/sa/新建文件夹.7z'
# with client.read(hdfs_path) as fs:
#     data = fs.read()
#     response = make_response(data)
#     response.headers.set('Content-Type', 'application/octet-stream')
#     response.headers["Content-Disposition"] = "attachment; filename={};".format("parameters")
#     return response
# pre_path, filename = os.path.split(hdfs_path)
# chunk_filename_list = [get_chunk_filename(prefix=pre_path, filename=filename, chunk_number=i) for i in
#                        range(1, 11 + 1)]
# with client.read(hdfs_path=chunk_filename_list[0]) as f:
#     client.write(hdfs_path=hdfs_path, data=f.read())
# for chunk_filename in chunk_filename_list[1:]:
#     with client.read(hdfs_path=chunk_filename) as f:
#         client.write(hdfs_path=hdfs_path, data=f.read(), append=True)
#
# if client.status(hdfs_path=hdfs_path, strict=False):
#             for chunk_filename in chunk_filename_list:
#                 client.delete(hdfs_path=chunk_filename)

# client.upload(hdfs_path=hdfs_path, local_path='E:/BaiduNetdiskDownload/新建文件夹 (2)/新建文件夹.7z')
# f = client.status(hdfs_path=hdfs_path, strict=False)
# print(client.checksum(hdfs_path))

import hashlib
import os


# def get_md5_01(file_path):
#     md5 = None
#     if os.path.isfile(file_path):
#         f = open(file_path, 'rb')
#         md5_obj = hashlib.md5()
#         md5_obj.update(f.read())
#         hash_code = md5_obj.hexdigest()
#         f.close()
#         md5 = str(hash_code).lower()
#     return md5
#
# print(get_md5_01('E:/BaiduNetdiskDownload/新建文件夹 (2)/新建文件夹.7z'))
#
# client.read()

# f = client.status(hdfs_path)['modificationTime']
#
# print(f)
# print(f[:10])
# print(f)
# print(f["modificationTime"])
# print(time.time())
# client.
# data = '''
# this is new file by lys！
# '''
#
#
# client.delete('/forkcloud/forkcloud-proxy/dataset/7/4/dataset.zip', recursive=True)
#
# with client.write('/forkcloud/forkcloud-proxy/dataset/7/4/dataset.zip') as writer:
#     with open('C:/Users/Administrator/Desktop/temp/dataset.zip', 'rb') as f:
#         writer.write(f.read())
with client2.read('/forkcloud/forkcloud-proxy/dataset/7/4/dataset.zip') as f:
        writer.write(f.read())
#
# client.
