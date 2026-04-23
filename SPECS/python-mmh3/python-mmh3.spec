# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mmh3

Name:           python-%{srcname}
Version:        5.2.1
Release:        %autorelease
Summary:        Python extension for MurmurHash
License:        MIT
URL:            https://github.com/hajimes/mmh3
#!RemoteAsset:  sha256:bbea5b775f0ac84945191fb83f845a6fd9a21a03ea7f2e187defac7e401616ad
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
mmh3 is a Python extension for MurmurHash (MurmurHash3),
a set of fast and robust non-cryptographic hash functions invented by Austin Appleby.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
