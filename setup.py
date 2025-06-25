import os
import setuptools

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def _get_version():
    with open(os.path.join(_CURRENT_DIR, "cbvf_reachability", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__") and "=" in line:
                version = line[line.find("=") + 1:].strip(" '\"\n")
                if version:
                    return version
        raise ValueError("`__version__` not defined in `cbvf_reachability/__init__.py`")


def _parse_requirements(file):
    with open(os.path.join(_CURRENT_DIR, file)) as f:
        return [line.rstrip() for line in f if not (line.isspace() or line.startswith("#"))]


setuptools.setup(name="cbvf_reachability",
                 version=_get_version(),
                 description="Hamilton-Jacobi reachability analysis for use in Control Barrier Value Functions in JAX.",
                 long_description=open("README.md").read(),
                 long_description_content_type="text/markdown",
                 author="Bartosz Jemioł",
                 author_email="b.s.jemiol@student.tudelft.nl",
                 url="https://github.com/Extrabartek/cbvf_reachabilityy",
                 license="MIT",
                 packages=setuptools.find_packages(),
                 install_requires=_parse_requirements("requirements.txt"),
                 python_requires="~=3.8")
