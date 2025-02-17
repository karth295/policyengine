from setuptools import setup, find_packages

setup(
    name="PolicyEngine",
    version="1.105.1",
    author="PolicyEngine",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url="https://github.com/policyengine/policyengine",
    install_requires=[
        "dpath<2.0.0,>=1.5.0",
        "flask",
        "flask_cors",
        "google-cloud-storage>=1.42.0",
        "google-cloud-logging",
        "gunicorn",
        "itsdangerous==2.0.1",
        "Jinja2==3.0.3",
        "kaleido",
        "microdf_python",
        "numpy",
        "OpenFisca-Core",
        "OpenFisca-Tools>=0.13.3",
        "OpenFisca-UK==0.30.0",
        "OpenFisca-US==0.148.0",
        "pandas",
        "plotly",
        "pytest",
        "rdbl",
        "tables",
        "wheel",
        "yaml-changelog>=0.2.0",
    ],
    packages=find_packages(),
)
