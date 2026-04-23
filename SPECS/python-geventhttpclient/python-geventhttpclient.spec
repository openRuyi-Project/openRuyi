# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname geventhttpclient

Name:           python-%{srcname}
Version:        2.3.9
Release:        %autorelease
Summary:        A high performance, concurrent http client library for python with gevent
License:        MIT
URL:            https://github.com/geventhttpclient/geventhttpclient
#!RemoteAsset:  sha256:16807578dc4a175e8d97e6e39d65a10b04b5237a8c55f7a5ef39044e869baeb8
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(httplib2)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A high performance, concurrent HTTP client library for python using gevent.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-MIT

%changelog
%autochangelog
