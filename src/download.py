__author__ = 'dk'
import os
import sys
import requests
import base64
import json
from config import  github_access_token
def download_file(repo, path, dst):
    print('Download {0} now!'.format(path))
    sys.stdout.flush()
    if os.path.exists(os.path.dirname(dst)) == False:
        os.makedirs(os.path.dirname(dst), True)

    url='https://api.github.com/repos/{0}/contents/{1}'.format(repo, path)
    headers = {
        'Accept':'application/vnd.github.v3+json',
        'Authorization':'token {0}'.format(github_access_token)
    }
    get = requests.get(url, headers = headers)
    with open(dst,'w') as fp:
        fp.write(base64.b64decode(get.json()['content']).decode())
    return  get.status_code

if __name__ == '__main__':
    url='https://raw.githubusercontent.com/jmhIcoding/Intra-domain-WPF/master/YouTube/D1_YouTube_compressed/D1_YouTube.z01'
    path = './YouTube/D1_YouTube_compressed/D1_YouTube.z01'
    download_file(url,dst=path)