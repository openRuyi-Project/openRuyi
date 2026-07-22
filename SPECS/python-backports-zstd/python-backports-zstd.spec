# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname backports-zstd
%global pypi_name backports_zstd

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        Backport of compression.zstd
License:        PSF-2.0 AND BSD-3-Clause
URL:            https://github.com/rogdham/backports.zstd
#!RemoteAsset:  sha256:80a7859ffe70bf239d7a2ce15293bdeb5b4280ff7dc326ffab312b0e254dbb24
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -C--build-option=--system-zstd
BuildOption(install):  -l backports

BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Backport of the compression.zstd module from Python 3.14.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%license LICENSE_zstd.txt

%changelog
%autochangelog
