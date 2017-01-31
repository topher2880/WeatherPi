import os

dpkg_path = '/var/lib/dpkg/info/'
paths = os.listdir(dpkg_path)
for path in paths:
    path = dpkg_path + path
    f = open(path, 'a+')
    data = f.read()
    if len(data) > 1 and data[-1:] != '\n':
        f.write('\n')
        print 'added newline character to:', path
    f.close()  
