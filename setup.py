from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='sheryel',
    version='0.0.1',
    description='A way too complicated command line interface (CLI) for printing sheryel words.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: FreeBSD License',
        'Programming Language :: Python :: 3.10'
    ],
    url='https://github.com/peaceknight05/sheryel',
    author='Shou Haruka',
    author_email='jonathantanatlol@gmail.com',
    license='FreeBSD',
    packages=["sheryel", "sheryel.output", "sheryel.utils"],
    package_data={"words": ["*.txt"]},
    zip_safe=False,
    entry_points={
        'console_scripts': ['sheryel=sheryel.cli.output:cli']
	},
    include_package_data=True
)