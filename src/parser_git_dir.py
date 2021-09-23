__author__ = 'dk'

from  github import Github
from conf.config import github_access_token
from urllib.parse import urlparse
from urllib.parse import urlencode
import tqdm
from src import download
def parser_git_directory(url):
    git = Github(login_or_token=github_access_token)
    repository = urlparse(url).path.split('/')[0]+ '/'.join(urlparse(url).path.split('/')[1:3])
    repo = git.get_repo(repository)
    dirs= repo.get_dir_contents('/'.join(urlparse(url).path.split('/')[3:]))
    download_urls = []
    filepaths = []
    for file_or_dir in dirs:

        try:
            contents =  repo.get_contents(file_or_dir.path)
            if contents.type == 'dir':
                ##说明是文件夹, 递归访问
                sub_url =  url.encode(url + file_or_dir.split('/')[-1])
                files, urls = parser_git_directory(sub_url)
                download_urls += urls
                filepaths += files

            else:
                ##说明是文件, 添加到文件的队列里面去
                download_urls.append(contents.download_url)
                filepaths.append(contents.path)
        except BaseException as exp:
            ##如果是大文件, 会报错; 或者这个文件夹内有超过1000个文件
                download_urls.append(file_or_dir.download_url)
                filepaths.append(file_or_dir.path)
    return filepaths, download_urls




if __name__ == '__main__':
    url='https://github.com/jmhIcoding/Intra-domain-WPF/YouTube/D1_YouTube_compressed'
    files, urls = parser_git_directory(url)
    for index in tqdm.trange(len(files)):
        file = files[index]
        url= urls[index]
        download.download_file(url=url, dst=file)