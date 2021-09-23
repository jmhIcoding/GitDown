__author__ = 'dk'
import tqdm
import argparse
from src import parser_git_dir
from conf import config

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('github_directory')