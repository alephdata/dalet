from setuptools import setup, find_packages


setup(
    name='dalet',
    version='1.2.1',
    description="A library with data parsers for aleph.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='names countries phones domains email country',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/alephdata/dalet',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'normality>=0.4.0',
        'pycountry==17.1.8',
        'urlnorm==1.1.4',
        'flanker>=0.3.4',
        'countrynames>=1.2',
        'parsedatetime==2.1',
        'phonenumbers>=8.3.3',
        'Babel==2.4.0',
        'six'
    ],
    tests_require=[
        'nose'
    ],
    entry_points={
    }
)
