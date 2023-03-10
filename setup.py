from setuptools import setup

setup(
    name='students',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'json',
    ],
    entry_points='''

        [console_scripts]
        students=main:cli
    ''',
)