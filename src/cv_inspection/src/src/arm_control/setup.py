from setuptools import setup

package_name = 'arm_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='youremail@example.com',
    description='Robotic arm control module for EV charging',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_commander = arm_control.arm_commander:main',
        ],
    },
)
