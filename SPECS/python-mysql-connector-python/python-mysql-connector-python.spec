# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mysql-connector-python
%global pypi_name mysql_connector_python

Name:           python-%{srcname}
Version:        9.7.0
Release:        %autorelease
Summary:        MySQL driver written in Python
License:        GPL-2.0-only WITH Universal-FOSS-exception-1.0
URL:            https://dev.mysql.com/doc/connector-python/en/
VCS:            git:https://github.com/mysql/mysql-connector-python.git
#!RemoteAsset:  sha256:933887e71c871b6e9d8908459fe8303ebcf8feb5cc1e1c49caa6490e525cf78e
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
# The C extension (_mysql_connector) is not built because openRuyi currently
# provides MariaDB Connector/C rather than Oracle MySQL C API as the system
# MySQL client library. The extension depends on MySQL 8/9-only C API symbols
# that MariaDB Connector/C does not expose. A pure Python build still provides
# the full mysql.connector module and all protocol-level features.
BuildArch:      noarch
BuildSystem:    pyproject

# Force pure Python wheel when C extension is disabled.
Patch2000:      2000-pure-python-wheel.patch

BuildOption(install):  -l mysql
# Skip OCI auth plugins: Package 'oci' is not installed.
BuildOption(check):  -e 'mysql.connector.plugins.authentication_oci_client'
BuildOption(check):  -e 'mysql.connector.aio.plugins.authentication_oci_client'
# Skip C-extension wrappers: _mysql_connector is not built.
BuildOption(check):  -e 'mysql.connector.connection_cext'
BuildOption(check):  -e 'mysql.connector.cursor_cext'
BuildOption(check):  mysql.connector

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(fido2)
BuildRequires:  python3dist(gssapi)
BuildRequires:  python3dist(langchain)
BuildRequires:  python3dist(langchain-core)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(opentelemetry-sdk)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlparse)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
MySQL Connector/Python enables Python programs to access MySQL databases using
an API that is compliant with the Python Database API Specification v2.0.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
