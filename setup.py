from setuptools import setup, find_packages

setup(
    name="seo",
    version="0.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        'django-solo',
    ],
)
