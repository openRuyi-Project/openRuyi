# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Beaker

Name:           python-beaker
Version:        1.14.1
Release:        %autorelease
Summary:        WSGI middleware layer to provide sessions
License:        BSD-3-Clause
URL:            https://github.com/bbangert/beaker
# No tests available on pypi
#!RemoteAsset:  sha256:886f52a51810703fdbc0a3e54fca40886288ff530b2070582edce72bf1945447
Source0:        https://files.pythonhosted.org/packages/source/b/beaker/beaker-%{version}.tar.gz
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
rm -rf tests/test_managers
rm -f tests/test_memcached.py
rm -f tests/test_cachemanager.py
rm -fv tests/test.db

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
