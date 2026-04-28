# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname portalocker

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Library to provide an easy API to file locking
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/portalocker
#!RemoteAsset:  sha256:1f3002956a54a8c3730586c5c77bf18fae4149e07eaf1c29fc3faf4d5a3f89ac
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Portalocker is a library to provide an easy API to file locking.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import -e portalocker.redis
# skip tests as there are many deps we don't have yet.

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%{?autochangelog}
