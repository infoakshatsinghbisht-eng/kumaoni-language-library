# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

long_desc = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_desc = fh.read()

setup(
    name="kumaoni",
    version="1.0.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="Kumaoni (कुमाऊँनी) Language Standard Library: 300,516+ Inflections, Voice AI, Speech Translation, and Himalayan Culture",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library",
    project_urls={
        "Homepage": "https://akshatsinghbisht.com/",
        "GitHub": "https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library",
        "LinkedIn": "https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/",
        "Amazon Author": "https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28",
        "ResearchGate": "https://www.researchgate.net/profile/Akshat-Bisht-8",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "kumaoni.lexicon": ["data/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
)
