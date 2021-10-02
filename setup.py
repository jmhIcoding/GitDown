#coding:utf8
import setuptools
import os
long_description=\
'''
A tool to download sub-dirs from github.

For more details, please refer to the homepage: https://github.com/jmhIcoding/GitDown.
'''
setuptools.setup(
    name='gitdown',
    version='1.1.9',
    description='A tool to download sub-dirs from github.',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmhIcoding/GitDown',
    author='jiangminghao',
    author_email='jiangminghao@iie.ac.cn',
    install_requires=[
        'pygithub',
        'requests',
        'tqdm'
    ],
    packages = setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'gitdown=gitdown.main:main'
        ]
    },
    classifiers=['Programming Language :: Python :: 3']
)