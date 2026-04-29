# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname srsly

Name:           python-%{srcname}
Version:        2.5.2
Release:        %autorelease
Summary:        Modern high-performance serialization utilities for Python
License:        MIT
URL:            https://github.com/explosion/srsly
#!RemoteAsset:  sha256:4092bc843c71b7595c6c90a0302a197858c5b9fe43067f62ae6a45bc3baa1c19
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Needs additional dependencies
BuildOption(check):  -e "srsly.tests.test_msgpack_api"
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(catalogue)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package bundles some of the best Python serialization
libraries into one standalone package, with a high-level API
that makes it easy to write code that's correct across platforms
and Pythons. This allows us to provide all the serialization utilities
we need in a single binary wheel. Currently supports JSON, JSONL,
MessagePack, Pickle and YAML.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
