import os

from src.user.constant import FCFolderType
from src.database import DbStore
from hdfs import InsecureClient
from src.utils import FormatConverter

class ScanOperations():
    def __init__(self, database=None):
        self._database = database or DbStore()
        self._hdfsClient = InsecureClient(url=os.getenv('HDFS_HOST_AND_PORT'), user='root')

    def storage_scan_by_userid(self, user_id, type, record):
        ls = self._database.get_dataset_folder_list_by_user_id(user_id=user_id, type=type)
        result_list = []
        totalUsage = 0
        for result in ls:
            usage = int(self._hdfsClient.content(FormatConverter.path_join(x_id=result.id, hdfs=True)).get("length"))
            totalUsage += usage
            data = {
                'name': result.name,
                'size': usage
            }
            result_list.append(data)
        if record:
            scan_time = self._database.record_dataset_folder_storage(user_id=user_id, type=type, size=totalUsage)
            return scan_time
        else:
            result_list.sort(key=lambda k: (k.get('size'), 0), reverse=True)
            finalList = [{'Total': FormatConverter.dynamic_file_size(totalUsage)}]
            if totalUsage == 0:
                return finalList
            length = 5 if len(result_list) > 5 else len(result_list)
            for i in range(length):
                result_list[i]['percent'] = round(float(result_list[i]['size'])*100/float(totalUsage), 2)
                result_list[i]['size'] = FormatConverter.dynamic_file_size(result_list[i]['size'])
                finalList.append(result_list[i])
            return finalList

    def global_storage_scan(self):
        users = self._database.get_users()
        for user in users:
            self.storage_scan_by_userid(user_id=user.id, type=FCFolderType.DATASET, record=True)
            self.storage_scan_by_userid(user_id=user.id, type=FCFolderType.PARAMETER, record=True)

    def __enter__(self):
        self.connect()

    def connect(self):
        self._database.connect()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def disconnect(self):
        self._database.disconnect()