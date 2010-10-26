from setuptools import setup, find_packages

version = __import__('alert_grid').__version__

setup(
    name = 'alert-grid',
    version = version,
    description = 'Alert Grid utility',
    author = 'Jonas Obrist',
    author_email = 'jonas.obrist@divio.ch',
    url = 'http://github.com/ojii/alert-grid',
    packages = find_packages(),
    zip_safe=False,
)