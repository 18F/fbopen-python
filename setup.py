
from setuptools import setup

setup(name="fbopen",
	version='0.0.1',
	description='Python access to the FBOpen API',
	url='http://github.com/18F/fbopen-python',
	author='18F.gsa.gov',
	zip_safe=False,
	install_requires=[
		'requests==2.3.0'
	],
    packages=['fbopen', 'fbopen.test'],
    package_dir={'fbopen': 'fbopen'},
    classifiers=['Development Status :: 2 - Pre-Alpha'],
    test_suite='fbopen.test',
    tests_require=[
        'dotenv'
    ]
)