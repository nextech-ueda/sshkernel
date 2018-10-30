import setuptools
from ssh_kernel import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssh_kernel",
    version=version,
    author="UENO, Masaru",
    author_email="m-ueno@users.noreply.github.com",
    description="SSH Kernel",
    install_requires=[
        'ipykernel>=5.0.0',
        'ipython>=7.0.0',           # install.py
        'jupyter_client>=5.2.0',    # install.py
        'metakernel>=0.20.0',
        'paramiko==2.4.*',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: IPython",
        "Topic :: System :: Shells",
        "License :: OSI Approved :: MIT License",
    ],
)
