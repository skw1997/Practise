import zipfile

import markdown
import codecs
import os
def md_to_html():
    # css = '''
    # <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    # '''
    # name = 'Readme_class'
    # in_file = '%s.md'%(name)
    # out_file = '%s.html' % (name)
    #
    # input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    # file = input_file.read()
    # html = markdown.markdown(file)
    #
    # out_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    # out_file.write(css+html)
    # path = 'abc.doc'
    # pre_path, filename = os.path.split(path)
    # name, ext = os.path.splitext(filename)
    # htmlname = name + '.html'
    # print(' ')
    stardir = 'D:\SaClassDemo'
    zip = 'D:\SaClassDemo\s.zip'
    print(zip_ya(stardir, zip))
def zip_ya( startdir, zip_path):
    z = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), os.path.join(fpath, filename))
    z.close()

if __name__ == '__main__':
    md_to_html()