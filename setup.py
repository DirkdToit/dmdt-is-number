import setuptools
import versioneer

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="dmdt_is-number",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Dirk du Toit",
    author_email="dirk@brightedge.co.za",
    description="A Python library to determine if something is a number.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
