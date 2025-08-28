from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="multimodal-financial-data-modelling",
    version="1.0.0",
    author="DeepRo",
    author_email="deepro2811@example.com",
    description="A comprehensive project for multimodal financial data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepro2811/MultimodalFinancialDataModelling",
    py_modules=["financial_data_collector"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="finance, data analysis, nse, stock market, machine learning, multimodal",
)