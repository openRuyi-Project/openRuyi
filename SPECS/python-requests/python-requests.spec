# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests

Name:           python-%{srcname}
Version:        2.32.5
Release:        %autorelease
License:        Apache-2.0
URL:            https://requests.readthedocs.io/
Summary:        Python HTTP library
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
Requests is a Python HTTP client library.  It aims to be easier to use
than Python’s urllib2 library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
