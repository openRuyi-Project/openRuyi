# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname msgpack

Name:           python-%{srcname}
Version:        1.1.2
Release:        %autorelease
Summary:        Python MessagePack (de)serializer
License:        Apache-2.0
URL:            https://msgpack.org/
#!RemoteAsset:  sha256:3b60763c1373dd60f398488069bcdc703cd08a711477b5d480eecc9f9626f47e
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  gcc-c++
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%prep -a
# There is a circular dependency with python-msgpack-ext
rm -rf test/test_timestamp.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog
