from setuptools import setup, find_packages


classifiers = [
	'Intended Audience :: GIS & Remote Sensing Technicians',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
]


setup(
	name='ndvi2gif',
	version='0.0.1',
	description='Python package to create ndvi seasonal composites, and download them as gif and geotiff',
	url='https://github.com/Digdgeo/GEE_Playground',
	python_requires='>=3.5',
	author='Diego Garcia Diaz',
	author_email='digd.geografo@gmail.com',
	license='MIT',
	install_requires=['geemap >= 0.6.10'],
	packages=find_packages(include=['ndvi2gif', 'ndvi2gif.*']),
	zip_safe=False
)