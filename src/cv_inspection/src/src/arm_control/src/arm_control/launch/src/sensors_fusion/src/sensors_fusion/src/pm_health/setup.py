from setuptools import setup
package_name = 'pm_health'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='your@email.com',
    description='Predictive Maintenance Node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['health_node = pm_health.health_node:main'],
    },
)
