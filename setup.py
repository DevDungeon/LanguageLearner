from setuptools import setup

setup(
    name='langlearn',
    version='1.0.0',
    description='Language learning tool',
    url='https://github.com/DevDungeon/LangLearn',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    packages=['langlearn'],
    scripts=[
        'bin/langlearn',
        'bin/langlearn.bat',
    ],
    package_data={
        'langlearn': [
            'vocabulary/*.txt',
        ],
    },
    zip_safe=False,
    install_requires=[
        'requests'
    ]
)
