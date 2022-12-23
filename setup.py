from setuptools import setup, find_packages
from os import path
import re

package_name="simpcamcap"
root_dir = path.abspath(path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setup(
    name=package_name,
    version=version,
    description=\
        "Very simple recording tool using only OpenCV. " +
        "Automatically record the camera capture to mp4, press C key or left mouse button click captures the image.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Katsuya Hyodo",
    author_email="rmsdh122@yahoo.co.jp",
    url="https://github.com/PINTO0309/simpcamcap",
    license="MIT License",
    packages=find_packages(exclude=['test*']),
    platforms=["linux", "unix"],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            "simpcamcap=simpcamcap:main"
        ]
    }
)