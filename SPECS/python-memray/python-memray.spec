# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname memray

Name:           python-%{srcname}
Version:        1.19.3
Release:        %autorelease
Summary:        A memory profiler for Python applications
License:        Apache-2.0
URL:            https://github.com/bloomberg/memray
#!RemoteAsset:  sha256:4e0fb29ff0a50c0ec9dc84294d8f2c83419feba561a37628b304c2ae4fe73d03
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(textual)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Memray is a memory profiler for Python applications.
It allows developers to track and analyze memory usage.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/memray*

%changelog
%autochangelog
