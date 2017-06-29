#!/usr/bin/env bash

set -e # Exit if an error occurs
set -u # Exit for an undefined variable

PKG_NAME={{cookiecutter.python_package_name}}
PROJECT_NAME={{cookiecutter.github_project_name}}

echo "installing jupyter"
pip install -U jupyter

echo "installing $PROJECT_NAME"
pip install .

echo "enabling $PKG_NAME"
jupyter nbextension enable --py --sys-prefix widgetsnbextension
jupyter nbextension enable --py --sys-prefix $PKG_NAME
