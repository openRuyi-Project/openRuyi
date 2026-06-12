# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname repoze-lru
%global pypi_name repoze_lru

Name:           python-%{srcname}
Version:        0.8
Release:        %autorelease
Summary:        Tiny LRU cache implementation and decorator
License:        LicenseRef-openRuyi-Repoze-BSD-derived
URL:            https://github.com/repoze/repoze.lru
VCS:            git:https://github.com/repoze/repoze.lru.git
#!RemoteAsset:  sha256:a252408cd93fe670c88d6665b96fe5d42e071dba2507a1f21a1e609ae4fa891a
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l repoze

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
repoze.lru is a LRU (least recently used) cache implementation. Keys and
values that are not used frequently will be evicted from the cache faster
than keys and values that are used frequently. It works under CPython and
PyPy, and provides a decorator for caching function results.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
