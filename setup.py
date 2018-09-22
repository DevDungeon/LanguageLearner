from setuptools import setup

setup(
    name='langlearn',
    version='1.0.1',
    description='Tool for practicing foreign language vocabulary and typing',
    url='https://github.com/DevDungeon/LanguageLearner',
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
