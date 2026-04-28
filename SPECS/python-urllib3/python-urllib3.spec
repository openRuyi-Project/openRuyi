# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname urllib3

Name:           python-%{srcname}
Version:        2.5.0
Release:        %autorelease
Summary:        HTTP library with thread-safe connection pooling
License:        MIT
URL:            https://urllib3.readthedocs.io/
#!RemoteAsset:  sha256:3fc47733c7e419d4bc3f6b3dc2b4f890bb743906a30d56ba4a5bfa4bbff92760
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No module named 'js'
BuildOption(check):  -e urllib3.contrib.emscripten
BuildOption(check):  -e 'urllib3.contrib.emscripten.*'
# No module named 'socks'
BuildOption(check):  -e urllib3.contrib.socks

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
# For tests
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(h2)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Urllib3 supports features left out of urllib and urllib2 libraries.  It
can reuse the same socket connection for multiple requests, it can POST files,
supports url redirection and retries, and also gzip and deflate decoding.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
