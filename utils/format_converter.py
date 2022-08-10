import math


class FormatConverter:
    @staticmethod
    def dynamic_file_size(file_size_bytes):
        if file_size_bytes == 0:
            return f'0 B'
        size_name = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
        unit = math.floor(math.log(file_size_bytes, 1024))
        data = round(file_size_bytes/pow(1024, unit), 2)
        return f'{data} {size_name[unit]}'

    @staticmethod
    def path_join(x_id, path=None, sub=None, hdfs=False):
        # strip initial and tailing '/' to avoid absolute path in path join
        if path is not None:
            path = path.strip('/')
        if sub is not None:
            sub = sub.strip('/')
        if not hdfs:
            if not sub:
                if not path:
                    path = '/root/dataset/{}'.format(str(x_id))
                else:
                    path = '/root/dataset/{}/{}'.format(str(x_id), path)
            elif not path:
                path = '/root/dataset/{}/{}'.format(str(x_id), sub)
            else:
                path = '/root/dataset/{}/{}/{}'.format(str(x_id), path, sub)
        else:
            if not sub:
                if not path:
                    path = '/forkcloud/forkcloud-proxy/dataset/{}'.format(str(x_id))
                else:
                    path = '/forkcloud/forkcloud-proxy/dataset/{}/{}'.format(str(x_id), path)
            elif not path:
                path = '/forkcloud/forkcloud-proxy/dataset/{}/{}'.format(str(x_id), sub)
            else:
                path = '/forkcloud/forkcloud-proxy/dataset/{}/{}/{}'.format(str(x_id), path, sub)
        return path

    @staticmethod
    def time_converter(start_time, end_time, min_minutes):
        min = min_minutes * 60
        start =
        return f'{data} {size_name[unit]}'