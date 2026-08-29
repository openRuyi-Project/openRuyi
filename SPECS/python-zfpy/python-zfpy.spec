# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zfpy

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Python bindings for zfp
License:        BSD-3-Clause
URL:            https://github.com/LLNL/zfp
#!RemoteAsset:  sha256:75c7014bdb2ad497a08846aaadca6d13de7c154a541c42557e52ec42030ca926
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Use system zfp headers instead of the bundled copy.
Patch2000:      2000-use-system-zfp-headers.patch

BuildOption(install):  -l zfpy

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  cmake(zfp)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Zfpy provides Python bindings for compressed numerical arrays using zfp.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%license NOTICE

%changelog
%autochangelog
