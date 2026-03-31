# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libclang

Name:           python-%{srcname}
Version:        18.1.1
Release:        %autorelease
Summary:        Python bindings for libclang
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/sighingnow/libclang
#!RemoteAsset:  sha256:a1214966d08d73d971287fc3ead8dfaf82eb07fb197680d8b3859dbbbbf78250
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l clang

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

Requires:       clang

%description
This package provides Python bindings for the Clang C library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.TXT
%doc README.md

%changelog
%{?autochangelog}
