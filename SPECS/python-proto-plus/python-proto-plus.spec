# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname proto-plus
%global pypi_name proto_plus

Name:           python-%{srcname}
Version:        1.28.4
Release:        %autorelease
Summary:        Pythonic wrapper for protocol buffers
License:        Apache-2.0
URL:            https://github.com/googleapis/proto-plus-python
#!RemoteAsset:  sha256:5ff7ecad828e032a491fcb86947801768e32237f99dd049b649965b892ae9a63
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l proto +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(protobuf) >= 6.33.5
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Proto Plus provides idiomatic Python wrappers around protocol buffer message
classes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
