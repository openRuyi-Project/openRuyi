# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jsonpointer

Name:           python-%{srcname}
Version:        2.4
Release:        %autorelease
Summary:        JSON Pointer implementation in Python
License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-pointer
#!RemoteAsset:  sha256:585cee82b70211fa9e6043b7bb89db6e1aa49524340dde8ad6b63206ea689d88
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
