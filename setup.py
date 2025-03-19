from setuptools import setup, find_packages

setup(
    name="nova-post",
    version="0.1.0",
    author="Dmytro Avrushchenko",
    author_email="trippyfren@gmail.com",
    description="Python SDK for working with the Nova Post API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TrippyFrenemy/nova_post",
    packages=find_packages(where="nova_post"),
    package_dir={"": "nova_post"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.9",
)
