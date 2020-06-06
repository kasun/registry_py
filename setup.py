import os
import re

from setuptools import find_packages, setup


def get_version():
    with open(os.path.join("registry_py", "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


with open("README.md") as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="registry-py",
    version=get_version(),
    description="Automatic class registration in Python",
    long_description_content_type="text/markdown",
    long_description=README,
    license="MIT",
    packages=find_packages(),
    author="Kasun Herath",
    author_email="kasunh01@gmail.com",
    keywords=["class registration", "registry", "plugins"],
    url="https://github.com/kasun/registry_py",
    download_url="https://pypi.org/project/registry-py/",
)


if __name__ == "__main__":
    setup(**setup_args)
