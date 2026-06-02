# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pysqlcipher3

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        DB-API 2.0 interface for SQLCIPHER 3.x
License:        zlib-acknowledgement
URL:            https://github.com/rigglemania/pysqlcipher3
#!RemoteAsset:  sha256:3c8033812655947ebf29a809ac5106b2bc69be0274eaccef6b58f4580c8d06c5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# https://github.com/rigglemania/pysqlcipher3/pull/38
Patch0:         0001-python313-compat.patch

BuildOption(install):  -l %{srcname}
# skip tests: test.support.TESTFN and test.support.unlink removed since python3.10
BuildOption(check):  -e 'pysqlcipher3.test*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pysqlcipher3 is an interface to the SQLite 3.x embedded relational database
engine with SQLCipher encryption support. It is almost fully compliant with
the Python database API version 2.0.

%files
%doc README.rst
%license LICENSE
%{python3_sitearch}/*

%changelog
%autochangelog
