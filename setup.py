import io
import os
from setuptools import find_packages, setup

REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0.0"

# Directly listing dependencies
REQUIRED = [
    "certifi==2024.2.2",
    "charset-normalizer==3.3.2",
    "colorama==0.4.6",
    "idna==3.7",
    "iniconfig==2.0.0",
    "numpy==1.26.2",
    "packaging==23.2",
    "pluggy==1.4.0",
    "pytest==8.0.0",
    "requests==2.31.0",
    "scapy==2.5.0",
    "scipy==1.11.4",
    "urllib3==2.2.1"
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = ""

about = {}
if not VERSION:
    prefix = "src"
    project_slug = "cicflowmeter"
    with open(os.path.join(here, prefix, project_slug, "__init__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name="cicflowmeter",
    version=about["__version__"],
    description="CICFlowMeter V3 Python Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["cicflowmeter=cicflowmeter.sniffer:main"],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)

