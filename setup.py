from setuptools import setup, find_packages

setup(
    name='movieday',
    version='0.0.1',
    install_requires=[
        'pyyaml',
        'click'
    ],
    author='SYUOZ',
    author_email='syuo88@googlegroups.com',
    url='https://github.com/ucbdrive/bdp-dev',
    description='Movie day schedule generator',
    license='BDD',
    packages=find_packages(),
    python_requires='>=3.4',
    entry_points='''
    [console_scripts]
    generate=movieday.generator:generate
    '''
)
