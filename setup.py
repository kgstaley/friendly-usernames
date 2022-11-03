from setuptools import setup

setup(
    name="friendly-usernames",
    version='0.1.0',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'run = main:cli'
        ]
    }
)