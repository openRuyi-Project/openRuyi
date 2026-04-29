# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-rapidjson
%global pypi_name python_rapidjson

Name:           python-%{srcname}
Version:        1.23
Release:        %autorelease
Summary:        Python wrapper around rapidjson
License:        MIT
URL:            https://github.com/python-rapidjson/python-rapidjson
#!RemoteAsset:  sha256:0f845daeb26be147f5720a8c410308235092bb4fbb81ea408aa77203e26296fb
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l rapidjson

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
RapidJSON is an extremely fast C++ JSON parser and
serialization library: this module wraps it into a Python 3 extension,
exposing its serialization/deserialization (to/from either bytes,
str or file-like instances) and JSON Schema validation capabilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{python3_sitearch}/rapidjson-stubs/__init__.pyi

%changelog
%autochangelog
