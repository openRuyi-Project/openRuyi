# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname preshed

Name:           python-%{srcname}
Version:        3.0.12
Release:        %autorelease
Summary:        Cython hash table that trusts the keys are pre-hashed
License:        MIT
URL:            https://github.com/explosion/preshed
#!RemoteAsset:  sha256:b73f9a8b54ee1d44529cc6018356896cff93d48f755f29c134734d9371c0d685
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(cymem)
BuildRequires:  python3dist(murmurhash)
BuildRequires:  python3dist(cython)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Simple but high performance Cython hash table mapping
pre-randomized keys to void* values. Inspired by Jeff Preshing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
