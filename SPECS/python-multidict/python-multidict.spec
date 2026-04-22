# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname multidict

Name:           python-%{srcname}
Version:        6.7.1
Release:        %autorelease
Summary:        MultiDict implementation
License:        Apache-2.0
URL:            https://github.com/aio-libs/multidict
#!RemoteAsset:  sha256:ec6652a1bee61c53a3e5776b6049172c53b6aaba34f18c9ad04f82712bac623d
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Multidict is dict-like collection of key-value pairs where key might occur more
than once in the container.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
