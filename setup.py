from setuptools import setup, find_packages


setup(
    name='sot',
    version='1.0',
    install_requires=[
        'watchdog',
        'read_and_close'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sot = sot.bin:run'
        ]
    }
)
