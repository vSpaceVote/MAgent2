import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magent",
    version="0.1.0",
    author="PettingZoo Team",
    author_email="justinkterry@gmail.com",
    description="Multi-Agent Reinforcement Learning environments with very large numbers of agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PettingZoo-Team/MAgent",
    keywords=["Reinforcement Learning", "game", "RL", "AI"],
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pygame>=2.0.0.dev6'
    ],
    requires_python='>=3.5',
    data_files = [("", ["LICENSE.txt"])],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
