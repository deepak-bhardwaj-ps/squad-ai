from setuptools import setup, find_packages

setup(
    name="squad-ai",
    version="0.1.0",
    description="A modular AI agentic framework.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Deepak Bhardwaj",
    author_email="your.email@example.com",
    url="https://github.com/deepak-bhardwaj-ps/squad-ai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=1.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Python Modules :: AI Agents",
    ],
    python_requires=">=3.12",
    keywords="ai, agents, framework, machine-learning",
    project_urls={
        "Bug Tracker": "https://github.com/deepak-bhardwaj-ps/squad-ai/issues",
        "Documentation": "https://github.com/deepak-bhardwaj-ps/squad-ai#readme",
        "Source Code": "https://github.com/deepak-bhardwaj-ps/squad-ai",
    },
)