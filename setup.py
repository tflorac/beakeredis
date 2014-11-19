from setuptools import setup, find_packages

setup(
    name='beaker_redis',
    version='0.0.1',
    description="Redis backend for Beaker",
    long_description="""
    Extending beaker (cache & session module) to use Redis backend
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities'
    ],
    keywords='Beaker',
    author='Alexander Pyatkin',
    author_email='asp@thexyz.net',
    url='https://github.com/aspyatkin/beaker_redis',
    license='MIT',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'redis>=2.10'
    ],
    entry_points="""
    # -*- Entry points: -*-
    [beaker.backends]
    redis = beaker_extensions.redis_:RedisManager
    """
)
