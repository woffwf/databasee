"""
2023
olha.myronovych.ir.2022@lpnu.ua
© Olha.Myronovych
"""

from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='Netflix company using flask',
    author='Olha Myronovych',
    author_email='olha.myronovych.ir.2022@lpnu.ua',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
