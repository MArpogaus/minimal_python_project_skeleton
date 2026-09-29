[![img](https://img.shields.io/github/contributors/MArpogaus/python-project-skeleton.svg?style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/graphs/contributors)
[![img](https://img.shields.io/github/forks/MArpogaus/python-project-skeleton.svg?style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/network/members)
[![img](https://img.shields.io/github/stars/MArpogaus/python-project-skeleton.svg?style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/stargazers)
[![img](https://img.shields.io/github/issues/MArpogaus/python-project-skeleton.svg?style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/issues)
[![img](https://img.shields.io/github/license/MArpogaus/python-project-skeleton.svg?style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/blob/main/LICENSE)
[![img](https://img.shields.io/github/actions/workflow/status/MArpogaus/python-project-skeleton/test.yaml.svg?label=test&style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/actions/workflows/test.yaml)
[![img](https://img.shields.io/github/actions/workflow/status/MArpogaus/python-project-skeleton/release.yaml.svg?label=release&style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/actions/workflows/release.yaml)
[![img](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg?logo=pre-commit&style=flat-square)](https://github.com/MArpogaus/python-project-skeleton/blob/main/.pre-commit-config.yaml)
[![img](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://linkedin.com/in/MArpogaus)

[![img](https://img.shields.io/pypi/v/minimal-python-project-skeleton.svg?style=flat-square)](https://pypi.org/project/minimal-python-project-skeleton)
[![img](https://img.shields.io/pypi/pyversions/minimal-python-project-skeleton.svg?style=flat-square)](https://pypi.org/project/minimal-python-project-skeleton)


# Minimal Python Project Skeleton

1.  [About The Project](#orgc3b490b)
2.  [Getting Started](#org45aa3cf)
    1.  [Installation](#orga09ebde)
3.  [Contributing](#org561a72f)
4.  [License](#org9c8af82)
5.  [Contact](#org2bbc609)
6.  [Acknowledgments](#org0fcb37a)


<a id="orgc3b490b"></a>

## About The Project

This folder structure should act as a simple starting point for your next python project.

    .
    ├── .envrc
    ├── .github
    │   ├── dependabot.yml
    │   └── workflows
    │       ├── docs.yaml
    │       ├── pre-commit.yaml
    │       ├── release.yaml
    │       └── test.yaml
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── README.org
    ├── docs
    │   ├── api.md
    │   └── index.md
    ├── mkdocs.yml
    ├── pyproject.toml
    ├── src
    │   └── minimal_python_project_skeleton
    │       └── __init__.py
    └── test
        └── test_func.py

    7 directories, 19 files

It contains just the minimum to get you started with a ready configured GitHub actions for automated [linting](<https://github.com/MArpogaus/minimal-python-project-skeleton/blob/main/.github/workflows/pre-commit.yaml>), [testing](<https://github.com/MArpogaus/minimal-python-project-skeleton/blob/main/.github/workflows/test.yaml>), [documenting](<https://github.com/MArpogaus/minimal-python-project-skeleton/blob/main/.github/workflows/docs.yaml>) with MkDocs and mike and [releasing](<https://github.com/MArpogaus/minimal-python-project-skeleton/blob/main/.github/workflows/release.yaml>) on PiPy.


<a id="org45aa3cf"></a>

## Getting Started

Use this template directly to [create a new GitHub repository](<https://github.com/new?template_name=minimal-python-project-skeleton&template_owner=MArpogaus>) or just clone the repository to your desired destination and start working on your new project.

The docs workflow publishes one docs version per branch to a `gh-pages` branch.  After the first push, set Settings -> Pages -> Source to *Deploy from a branch*: `gh-pages`, `/ (root)`.  The site root works after the first push to `main`.

I have marked all the relevant parts that you might want to adjust.

    .github/workflows/release.yaml:      url: https://pypi.org/p/minimal-python-project-skeleton  # TODO: Replace with your PyPI project name
    .github/workflows/release.yaml:      url: https://test.pypi.org/p/minimal-python-project-skeleton  # TODO: Replace with your TestPyPI project name
    docs/api.md:<!-- TODO: Change package name -->
    mkdocs.yml:site_name: minimal_python_project_skeleton  # TODO: Change project name
    mkdocs.yml:repo_url: https://github.com/MArpogaus/minimal_python_project_skeleton  # TODO: Change project repo
    pyproject.toml:dependencies = []  # TODO: Add dependencies
    pyproject.toml:license = { text = "MIT" }  # TODO: Choose license
    pyproject.toml:name = "minimal_python_project_skeleton"  # TODO: Change package name
    pyproject.toml:  'minimal_python_project_skeleton[test]',  # TODO: Change package name
    pyproject.toml:Changelog = "https://github.com/MArpogaus/minimal_python_project_skeleton/blob/dev/CHANGELOG.md"  # TODO: Change project repo
    pyproject.toml:Documentation = "https://marpogaus.github.io/minimal_python_project_skeleton"  # TODO: Change project repo
    pyproject.toml:Issues = "https://github.com/MArpogaus/minimal_python_project_skeleton/issues"  # TODO: Change project repo
    pyproject.toml:Repository = "https://github.com/MArpogaus/minimal_python_project_skeleton"  # TODO: Change project repo

**Pro-Tipp:** If you later want to update the template, keep a separate branch (i.e. `skeleton`) around and `cherry-pick` the changes you would like to keep for future projects.
This way you can also pull the latest version from upstream and `checkout` the new files you would like to use in your project.


<a id="orga09ebde"></a>

### Installation

This package is available on [PyPI](https://pypi.org/project/minimal-python-project-skeleton/). You install it using pip:

    pip install minimal_python_project_skeleton


<a id="org561a72f"></a>

## Contributing

Any Contributions are greatly appreciated! If you have a question, an issue or would like to contribute, please read our [contributing guidelines](https://github.com/MArpogaus/minimal_python_project_skeleton/blob/main/CONTRIBUTING.md).


<a id="org9c8af82"></a>

## License

Distributed under the [MIT License](https://github.com/MArpogaus/minimal_python_project_skeleton/blob/main/LICENSE)


<a id="org2bbc609"></a>

## Contact

[Marcel Arpogaus](https://github.com/MArpogaus/) - [znepry.necbtnhf@tznvy.pbz](mailto:znepry.necbtnhf@tznvy.pbz) (encrypted with [ROT13](<https://rot13.com/>))

Project Link:
<https://github.com/MArpogaus/python-project-skeleton>


<a id="org0fcb37a"></a>

## Acknowledgments

-   README inspired by [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)
-   Contribution guidelines inspired by [probabilists/zuko](https://github.com/probabilists/zuko/)
-   Release workflow inspired by [packaging.python.org](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
