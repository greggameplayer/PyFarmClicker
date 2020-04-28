import os
import sys

from cx_Freeze import Executable
from cx_Freeze import setup

os.system("py -m pip install --upgrade pip")
os.system("py -m pip install -r requirements.txt")
build_exe_options = {
    "includes": [],
    "optimize": 2,
    "include_files": [("resources", "resources")],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        "__main__.py",
        base=base,
        icon="resources/images/logo.ico",
        targetName="PyFarmClicker",
    )
]

setup(
    name="PyFarmClicker",
    version="1.0.0",
    packages=["PyFarmClicker"],
    description="A farming themed clicker game written in python 3",
    author="Gregoire Hage",
    author_email="gregoire.hage@epsi.fr",
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["cx_Freeze"],
    options={"build_exe": build_exe_options},
    executables=executables,
)
