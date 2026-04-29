# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types-dataclasses

Name:           python-%{srcname}
Version:        0.6.6
Release:        %autorelease
Summary:        Typing stubs for dataclasses
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:4b5a2fcf8e568d5a1974cd69010e320e1af8251177ec968de7b9bb49aa49f7b9
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  dataclasses-stubs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Typeshed contains external type annotations for the Python standard library and
Python builtins, as well as third-party packages that are contributed by people
external to those projects.

%check
# Keep an explicit empty %%check here: this is a type stubs package, so the
# default pyproject import check would not exercise any meaningful runtime
# module surface.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md

%changelog
%autochangelog
