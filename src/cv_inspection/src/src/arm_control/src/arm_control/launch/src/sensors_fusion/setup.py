from setuptools import setup
package_name = 'sensors_fusion'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='your@email.com',
    description='Sensor fusion node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['fusion_node = sensors_fusion.fusion_node:main'],
    },
)
