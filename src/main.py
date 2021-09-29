__author__ = 'dk'
import argparse
from parser_git_dir import *
import download
import tqdm
import os

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('github_directory')

    parsed_args = args.parse_args()

    url= parsed_args.github_directory
    files, urls = parser_git_directory(url)

    for index in tqdm.trange(len(files)):
        file = files[index]
        url= urls[index]
        if os.path.exists(file) == True:
           print('{0} already download!'.format(file))
           continue
        download.download_file(url=url, dst=file)

        if os.path.exists(file) == False:
            print('{0} download fail! it will be re-download.'.format(file))
            files.append(file)

