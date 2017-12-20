# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

SETUP_KWARGS = dict(
    name='temboard',
    version='1.1',
    description='temBoard User Interface.',
    author='Julien Tachoires, Étienne BERSAC',
    license='PostgreSQL',
    scripts=['temboard'],
    install_requires=[
        'python-dateutil>=1.5',
        'psycopg2>=2.5.4',
        'sqlalchemy>=0.9.8',
        'tornado>=3.2',
    ],
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/dalibo/temboard/',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: System :: Monitoring",
    ],
    data_files=[
        ('share/temboard', [
            'share/create_repository.sh',
        ]),
        ('share/temboard/sql/', [
            'share/sql/application.sql',
            'share/sql/dev-fixture.sql',
            'share/sql/monitoring.sql',
        ]),
        ('share/temboard/quickstart/', [
            'share/temboard_CHANGEME.key',
            'share/temboard_CHANGEME.pem',
            'share/temboard_ca_certs_CHANGEME.pem',
            'share/temboard.conf',
            'share/temboard.logrotate',
        ]),
        ('lib/systemd/system', ['packaging/temboard.service']),
        # Installation from sources
        ('/usr/share/temboard', [
            'share/temboard.conf',
            'share/temboard.logrotate',
            'share/create_repository.sh',
        ]),
        ('/usr/share/temboard/sql/', [
            'share/sql/application.sql',
            'share/sql/monitoring.sql',
        ]),
        ('/usr/share/temboard/quickstart/', [
            'share/temboard_CHANGEME.key',
            'share/temboard_CHANGEME.pem',
            'share/temboard_ca_certs_CHANGEME.pem',
        ]),
    ],
)

if __name__ == '__main__':
    setup(
        long_description=open('README.rst').read(),
        packages=find_packages(),
        **SETUP_KWARGS
    )
