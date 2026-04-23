# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname curl_cffi

Name:           python-curl_cffi
Version:        0.14.0
Release:        %autorelease
Summary:        Python binding for curl-impersonate fork via cffi
License:        MIT
URL:            https://github.com/lexiforest/curl_cffi
#!RemoteAsset:  sha256:5ffbc82e59f05008ec08ea432f0e535418823cda44178ee518906a54f27a5f0f
Source:         https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
# it is arch specific since it depends on C FFI lib
BuildSystem:    pyproject

# use dynamic libs instead of static ones
Patch0:         0001-curl_cffi-use-system-dynamic-libs.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  curl-impersonate-chrome
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(certifi)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       curl-impersonate-chrome

%description
%{summary}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/curl-cffi

%changelog
%autochangelog
