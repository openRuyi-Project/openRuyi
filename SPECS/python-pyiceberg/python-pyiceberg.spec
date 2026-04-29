# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyiceberg

Name:           python-%{srcname}
Version:        0.11.1
Release:        %autorelease
Summary:        Official Apache Iceberg SDK for Python
License:        Apache-2.0
URL:            https://py.iceberg.apache.org/
VCS:            git:https://github.com/apache/iceberg-python.git
#!RemoteAsset:  sha256:366fe0d5a74e3cf1d4e7cbf3c49e308da60e7835ea268667be9185388f05d7a5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No module named 'pyarrow._s3fs'
BuildOption(check):  -e pyiceberg.io.pyarrow
BuildOption(check):  -e pyiceberg.catalog.bigquery_metastore

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(thrift)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyIceberg is a Python library for programmatic access to
Iceberg table metadata as well as to table data in Iceberg format.
It is a Python implementation of the Iceberg table spec.

%pyproject_extras_subpkg -n python-pyiceberg glue

%generate_buildrequires
%pyproject_buildrequires -x glue

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pyiceberg
%{python3_sitearch}/fb303/
%{python3_sitearch}/hive_metastore/

%changelog
%autochangelog
