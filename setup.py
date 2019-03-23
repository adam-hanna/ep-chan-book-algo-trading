import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="ep_chan_scripts",
        version="0.0.1",
        author="Adam Hanna",
        author_email="ahanna@mba2016.hbs.edu",
        description="This package provides ep chan's scripts in python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="",
        packages=setuptools.find_packages('src'),
        install_requires=[
            "ipykernel==4.8.2",
            "bokeh==0.12.15",
            "lxml==4.2.1",
            "mysql-connector-python==8.0.11",
            "pandas-datareader==0.6.0",
            "pipdeptree==0.12.1",
            "seaborn==0.8.1",
            "SQLAlchemy==1.2.7",
            "bs4==0.0.1",
            "pykalman==0.9.5",
            "pandas",
            "numpy",
            "tushare",
            "quandl",
            "arch",
            "psycopg2",
            "statsmodels==0.9.0",
        ],
        test_suite='nose.collector',
        tests_require=['nose'],
        classifiers=[
            "Programming Language :: Python :: 2",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
