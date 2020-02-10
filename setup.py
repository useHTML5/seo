from setuptools import setup, find_packages

setup(
    name="seo",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "django>=2.2",
        'django-solo',

    ],
)
