__author__ = 'dk'

from urllib.parse import urlparse

from  github import Github
import tqdm
import os
from config import github_access_token
import download


def parser_git_directory(url):
    git = Github(login_or_token=github_access_token)
    print(github_access_token)
    repository = urlparse(url).path.split('/')[0]+ '/'.join(urlparse(url).path.split('/')[1:3])
    repo = git.get_repo(repository)
    dirs= repo.get_dir_contents('/'.join(urlparse(url).path.split('/')[3:]))
    download_urls = []
    filepaths = []
    for file_or_dir in dirs:

            if file_or_dir.type == 'dir':
                ##说明是文件夹, 递归访问
                sub_url =  url.encode(url + file_or_dir.split('/')[-1])
                files, urls = parser_git_directory(sub_url)
                download_urls += urls
                filepaths += files

            else:
                ##说明是文件, 添加到文件的队列里面去
                download_urls.append(file_or_dir.download_url)
                filepaths.append(file_or_dir.path)
    return filepaths, download_urls

if __name__ == '__main__':
    url='https://github.com/jmhIcoding/Intra-domain-WPF/YouTube/D2_YouTube_compressed'
    files, urls = parser_git_directory(url)

    for index in tqdm.trange(len(files)):
        file = files[index]
        url= urls[index]
        if os.path.exists(file) == True:
           print('{0} already download!'.format(file))
           continue
        download.download_file(url=url, dst=file)

