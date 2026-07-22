# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tinycss2

Name:           python-%{srcname}
Version:        1.5.1
Release:        %autorelease
Summary:        Tiny CSS parser
License:        BSD-3-Clause
URL:            https://github.com/Kozea/tinycss2
#!RemoteAsset:  sha256:d339d2b616ba90ccce58da8495a78f46e55d4d25f9fd71dfd526f07e7d53f957
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l tinycss2

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(webencodings)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tinycss2 is a low-level CSS parser and generator written in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
