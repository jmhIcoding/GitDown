import setuptools
__author__ = 'jmh081701'

setuptools.setup(
    name='gitdown',
    version='1.1.2',
    description='A tool to download sub-dirs from github.',

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