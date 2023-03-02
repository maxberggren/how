from setuptools import setup

setup(
    name="how",
    version="0.1.0",
    py_modules=["how.cli"],
    entry_points={"console_scripts": ["how=how.cli:ask_gpt"]},
    install_requires=["requests", "rich"],
)