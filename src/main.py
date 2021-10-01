__author__ = 'dk'
import argparse
from parser_git_dir import *
import download
import tqdm
import os
import threading

lock = threading.Semaphore(1)
files = []
sem = None
def down(repo, file):
    global  sem, lock, files

    download.download_file(repo= repo, path= file, dst=file)
    if os.path.exists(file) == False:
        print('{0} download fail! it will be re-download in the future!'.format(file))
        lock.acquire()
        files.append(file)
        lock.release()

    sem.release()

if __name__ == '__main__':

    args = argparse.ArgumentParser(description='Download github resposity directory.')
    args.add_argument('--repo', type= str, required= True, help='Something like https://github.com/jmhIcoding/social_webpage')
    args.add_argument('--directory', type=str, required= True, help='Something like pcaps/. Note that do not start with "/" and end with "/", use "" (empty) for root directory.')
    args.add_argument('--thread_num', type=int, default= 5, help='The thread number for download!')
    parsed_args = args.parse_args()

    if parsed_args.directory[0] == '/' or parsed_args.directory[-1]== '/' :
        raise  ValueError('Oh, directory parameter must not start with "/" and end with "/"!, please refer to the help information.')

    if parsed_args.thread_num < 1:
        raise  ValueError('Oh, thread number should >= 1 ! ')

    repo = '/'.join(parsed_args.repo.split('/')[-2:])
    files = parser_git_directory(_repo= repo, directory= parsed_args.directory)

    sem = threading.Semaphore(parsed_args.thread_num)
    threads_list = []
    index = 0
    pbar = tqdm.tqdm(total=len(files))
    while index < len(files):
        pbar.update(1)
        file = files[index]
        index += 1
        if os.path.exists(file) == True:
           print('{0} already download!'.format(file))
           continue

        th = threading.Thread(target=down, args=(repo, file))
        sem.acquire()
        th.start()
        threads_list.append(th)

        if len(files)!= pbar.total:
            pbar.total = len(files)
            pbar.refresh()





