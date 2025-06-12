from setuptools import setup
import os
from glob import glob

package_name = 'cv_inspection'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='your@email.com',
    description='CV node for EV charging arm',
    license='MIT',
    entry_points={
        'console_scripts': [
            'inspection_node = cv_inspection.src.inspection_node:main',
        ],
    },
)
