from setuptools import setup, find_packages

setup(
    name="kumaoni",
    version="1.0.0",
    description="A standard-library-style Python package for Kumaoni language processing, linguistics, and universal translation.",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "kumaoni.lexicon": ["data/*.json"],
        "kumaoni.web": ["static/*"],
    },
    entry_points={
        "console_scripts": [
            "kumaoni=kumaoni.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
)
