from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'Flask>=1.0,<1.1',
        'gunicorn>=19,<20'
    ]
)
