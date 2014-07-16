from setuptools import setup

setup(
    name='timesheet',
    entry_points={
        'console_scripts': ['timesheet = timesheet.timesheet:main']},
    version='0.0.1',
    author='John Beieler',
    author_email='john.b30@gmail.com',
    license='LICENSE',
    description='Utility for managing timesheets.',
    long_description=open('README.md').read())
