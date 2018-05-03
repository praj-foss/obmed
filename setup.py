from setuptools import setup
import obmed

setup(
    name="obmed",
    version=obmed.__version__,
    description="Openbox menu editor",
    author="Priyadarshi Raj",
    license="MIT",

    packages=["obmed"],
    install_requires=["docopt"],

    entry_points={
        "console_scripts": [
            "obmed = obmed.run:main"
        ]
    }
)
