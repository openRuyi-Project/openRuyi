# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Beaker

Name:           python-beaker
Version:        1.13.0
Release:        %autorelease
Summary:        WSGI middleware layer to provide sessions
License:        BSD-3-Clause
URL:            https://github.com/bbangert/beaker
# No tests available on pypi
#!RemoteAsset:  sha256:e956cd8a35ad5de1b5212c7bff8fc01e2b3d34ab92466d24684c666abb8c9c30
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://github.com/bbangert/beaker/issues/242
Patch0:         0001-Avoid-using-dbm.sqlite3.patch

BuildOption(install):  beaker
BuildOption(check):  -e 'beaker.crypto.jcecrypto*'
BuildOption(check):  -e 'beaker.crypto.nsscrypto*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pycryptodome)
BuildRequires:  python3dist(cryptography)
# unsupported locale setting it_IT.UTF-8
BuildRequires:  glibc-locale

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%generate_buildrequires
%pyproject_buildrequires

%check -p
# needs mongo and redis running
rm -r tests/test_managers
rm tests/test_memcached.py
rm tests/test_cachemanager.py
rm -fv tests/test.db

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
