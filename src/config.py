__author__ = 'dk'
import os
from  github import Github
import github

config_path = os.path.expanduser('~') + '/gitdown.token'
if os.path.exists(config_path) == False:
    token = input('Please input your github access token now, first time:')

    try:
        git = Github(login_or_token=token)
        git.get_repo('helloworld9992939329392939294333435452dhfhdfjdfdgfgdfgfd___dfdf')
    except github.GithubException as exp:
        if isinstance(exp, github.BadCredentialsException):
            raise  ValueError('The token you input is invalid!!!')
    with open(config_path,'w') as fp:
        fp.write(token)

else:
    with open(config_path) as fp:
        token = fp.read()

github_access_token= token #github访问的token
