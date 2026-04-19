from setuptools import setup

package_name = 'llm_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[
        'controller',
        'model',
        'ros_interface',
        'view'
    ],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jessyca',
    description='LLM-based robot controller (Level 1)',
    entry_points={
        'console_scripts': [
            'run_llm = main:main',
        ],
    },
)

