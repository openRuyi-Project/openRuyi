# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cachetools

Name:           python-%{srcname}
Version:        6.2.2
Release:        %autorelease
Summary:        Extensible memoizing collections and decorators
License:        MIT
URL:            https://github.com/tkem/cachetools
#!RemoteAsset:  sha256:8e6d266b25e539df852251cfd6f990b4bc3a141db73b939058d809ebd2590fc6
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache
function decorator.

This module provides multiple cache implementations based on different
cache algorithms, as well as decorators for easily memoizing function
and method calls.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
