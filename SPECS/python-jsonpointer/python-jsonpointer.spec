# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonpointer

Name:           python-%{srcname}
Version:        3.1.1
Release:        %autorelease
Summary:        JSON Pointer implementation in Python
License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-pointer
#!RemoteAsset:  sha256:0b801c7db33a904024f6004d526dcc53bbb8a4a0f4e32bfd10beadf60adf1900
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
JSON Pointer is a Library to resolve JSON Pointers according to RFC 6901.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md AUTHORS
%license LICENSE.txt
%{_bindir}/jsonpointer

%changelog
%autochangelog
