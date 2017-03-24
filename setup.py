from setuptools import setup

setup(
    name='monorepo',
    version='0.1',
    py_modules=['monorepo'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        monorepo=monorepo:cli
    ''',
)
