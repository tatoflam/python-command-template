from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="page_tester",
    version="0.1.0",
    license="CC BY-ND 4.0",
    description="base project for python batch",
    author="tatoflam",
    url="",
    packages=find_packages("command_sample"),
    package_dir={"": "command_sample"},
    py_modules=[splitext(basename(path))[0] for path in glob('command_sample/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)