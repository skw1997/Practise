import os


def file_chunk_merge(x_id, total_chunk_number, path):
    if total_chunk_number < 1:
        pass
    path = path_join(x_id=x_id, path=path, )
    print(path)
    try:
        merge_file = open(path, 'wb')
        pre_path, filename = os.path.split(path)
        print(pre_path, filename)
        chunk_filename_list = [get_chunk_filename(prefix=pre_path, filename=filename, chunk_number=i) for i in
                               range(1, total_chunk_number + 1)]
        for chunk_filename in chunk_filename_list:
            with open(chunk_filename, 'rb') as f:
                merge_file.write(f.read())
    except Exception:
        pass
    finally:
        if merge_file:
            merge_file.close()

    # merge成功后，删除chunk file
    for chunk_filename in chunk_filename_list:
        os.remove(chunk_filename)
    return 1


def get_chunk_filename(prefix, filename, chunk_number):
    chunk_filename = filename + '-' + str(chunk_number)
    if chunk_filename.startswith(prefix):
        return chunk_filename
    return os.path.join(prefix, chunk_filename)


def get_merge_filename(prefix, filename):
    if filename.startswith(prefix):
        return filename
    return prefix + filename

def path_join(x_id, path=None, sub=None):
        if not sub:
            if not path:
                path = os.path.join('E:\\', str(x_id))
            else:
                path = os.path.join('E:\\', str(x_id), path)
        elif not path:
            path = os.path.join('E:\\', str(x_id), sub)
        else:
            path = os.path.join('E:\\', str(x_id), path, sub)

        return path

if __name__ == "__main__":
    pre_path, filename = os.path.split('s/test-bin-1-0.7G.zip/')
    print(pre_path)
    print(filename)
    chunk_filename = filename + '-' + str(1)
    print(chunk_filename)
    a = path_join(path=pre_path, x_id= 8, sub=chunk_filename)
    print(a)