__author__ = 'dk'
from  github import Github
from gitdown.config import github_access_token

def parser_git_directory(_repo, directory):
    git = Github(login_or_token=github_access_token)
    repository = _repo
    repo = git.get_repo(repository)
    directory  =  directory
    dirs= repo.get_dir_contents( '/' + directory)
    filepaths = []
    for file_or_dir in dirs:
            print('Go deep into {0}'.format(directory))
            if file_or_dir.type == 'dir':
                ##说明是文件夹, 递归访问
                sub_url =  directory + '/' + file_or_dir.path.split('/')[-1]
                files = parser_git_directory(_repo, sub_url)
                filepaths += files

            else:
                ##说明是文件, 添加到文件的队列里面去
                filepaths.append(file_or_dir.path)
    return filepaths

