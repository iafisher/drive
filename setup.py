from setuptools import setup, find_packages


setup(
    name='drive',
    version='0.1.0',
    description='Sync Google Drive files on Linux',
    license='MIT',
    author='Ian Fisher',
    author_email='iafisher@protonmail.com',
    entry_points={
        'console_scripts': [
            'pydrive = drive.main:main',
        ],
    },
    packages=find_packages(),
    project_urls={
        'Source': 'https://github.com/iafisher/drive',
    },
)
