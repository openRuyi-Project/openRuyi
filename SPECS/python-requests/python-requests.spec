# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests

Name:           python-%{srcname}
Version:        2.33.1
Release:        %autorelease
Summary:        Python HTTP library
License:        Apache-2.0
URL:            https://requests.readthedocs.io/
#!RemoteAsset:  sha256:18817f8c57c6263968bc123d237e3b8b08ac046f5456bd1e307ee8f4250d3517
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Requests is a Python HTTP client library.  It aims to be easier to use
than Python’s urllib2 library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
