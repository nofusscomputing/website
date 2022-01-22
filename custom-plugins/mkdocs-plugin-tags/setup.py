"""
Setup the plugin
"""
from setuptools import setup, find_packages

setup(
    version='0.0.1',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs==1.2.3',
    ],
    packages=find_packages(exclude=['*.tests']),
    package_data={'tags': ['templates/*.md.template']},
    entry_points={
        'mkdocs.plugins': [
            'tags = tags.plugin:TagsPlugin'
        ]
    }
)
