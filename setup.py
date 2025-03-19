from setuptools import setup, find_packages

setup(
    name="nova-post",
    version="0.2.2",
    author="Dmytro Avrushchenko",
    author_email="trippyfren@gmail.com",
    description="Python SDK for working with the Nova Post API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TrippyFrenemy/nova_post",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fake-useragent>=2.1.0",
        "pydantic>=2.10.6",
        "requests>=2.32.3",
    ],
    python_requires=">=3.9",
)
