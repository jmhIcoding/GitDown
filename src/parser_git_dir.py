__author__ = 'dk'

from urllib.parse import urlparse

from  github import Github
import tqdm
import os
from src.config import github_access_token
from src import  download


def parser_git_directory(repo, directory):
    git = Github(login_or_token=github_access_token)
    repository = repo
    repo = git.get_repo(repository)
    directory  = '/' + directory
    dirs= repo.get_dir_contents(directory)
    download_urls = []
    filepaths = []
    for file_or_dir in dirs:

            if file_or_dir.type == 'dir':
                ##说明是文件夹, 递归访问
                sub_url =  url + '/' + file_or_dir.path.split('/')[-1]
                files, urls = parser_git_directory(sub_url)
                download_urls += urls
                filepaths += files

            else:
                ##说明是文件, 添加到文件的队列里面去
                download_urls.append(file_or_dir.download_url)
                filepaths.append(file_or_dir.path)
    return filepaths, download_urls

