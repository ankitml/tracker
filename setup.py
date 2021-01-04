import os
import subprocess
from datetime import date

from setuptools import find_packages, setup


def version():
    """
    Since the version doesn't matter, we'll go with the following scheme:
    <year>.<month>.<day>[.dev0+g<short sha>]
    where g means git and <short sha> is sha[:7], if provided.
    This is inspired by setuptools_scm but since our build system doesn't
    copy .git into the Dockerfile, we can't use git tags. We must then
    rely on the `--build-arg SHA` and treat it as optional.
    Version Scheme PEP: https://www.python.org/dev/peps/pep-0440/
    """
    sha = os.environ.get("SHA")
    if sha is None:
        # we're probaby in a local dev environment
        try:
            stdout = subprocess.check_output(["git", "rev-parse", "HEAD"])
            sha = stdout.decode("utf-8").strip()
        except subprocess.CalledProcessError:
            # but we don't care if the command fails
            pass

    suffix = ""
    if sha is not None:
        # according to PEP-440, we must put .devN, so we choose N=0
        suffix = f".dev0+g{sha[:7]}"

    today = date.today()
    return f"{today.year}.{today.month}.{today.day}{suffix}"


setup(
    name="tracker",
    description="meal, mood and pain tracker",
    version=version(),
    # this will find all folders with a `__init__.py` in them, under
    # the app/isc directory.
    packages=find_packages(where="src"),
    # this tells setuptools to look in the src/isc/ directory when finding
    # python packages
    package_dir={"": "src"},
    entry_points = {
        "console_scripts": ["manage.py=tracker.manage:main"],
    },
    # this will include extra files in the built distribution
    install_requires=[],
)

