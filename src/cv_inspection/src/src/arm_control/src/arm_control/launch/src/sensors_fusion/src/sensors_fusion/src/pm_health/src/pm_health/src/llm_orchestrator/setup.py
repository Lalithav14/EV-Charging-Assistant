from setuptools import setup
package_name = 'llm_orchestrator'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lalitha V',
    maintainer_email='your@email.com',
    description='LLM orchestration node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['orchestrator = llm_orchestrator.orchestrator:main'],
    },
)
