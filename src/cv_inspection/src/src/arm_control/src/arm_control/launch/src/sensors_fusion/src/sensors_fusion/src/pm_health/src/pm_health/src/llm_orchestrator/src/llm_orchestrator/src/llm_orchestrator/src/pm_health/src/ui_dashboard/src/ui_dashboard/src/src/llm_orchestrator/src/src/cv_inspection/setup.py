from setuptools import setup
package_name = 'cv_inspection'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='your@email.com',
    description='Computer vision for EV plug detection',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['inspection_node = cv_inspection.inspection_node:main'],
    },
)
