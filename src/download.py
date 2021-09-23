__author__ = 'dk'
import os
import sys
def download_file(url, dst):
    if os.path.exists(os.path.dirname(dst)) == False:
        os.makedirs(os.path.dirname(dst))
    cmd = 'curl -LJ# {0} -o {1}'.format(url, dst)
    print('Downloading: {0}'.format(url), flush=True)
    os.system(cmd)


if __name__ == '__main__':
    url='https://raw.githubusercontent.com/jmhIcoding/Intra-domain-WPF/master/YouTube/D1_YouTube_compressed/D1_YouTube.z01'
    path = './YouTube/D1_YouTube_compressed/D1_YouTube.z01'
    download_file(url,dst=path)