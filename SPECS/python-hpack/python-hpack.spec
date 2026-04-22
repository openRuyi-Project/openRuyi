# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hpack

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Pure-Python HPACK header compression
License:        MIT
URL:            https://github.com/python-hyper/hpack
#!RemoteAsset:  sha256:ec5eca154f7056aa06f196a557655c5b009b382873ac8d1e66e79e87535f1dca
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HTTP/2 Header Encoding for Python This module contains a pure-Python
HTTP/2 header encoding (HPACK) logic for use in Python programs that implement
HTTP/2. It also contains a compatibility layer that automatically enables the
use of nghttp2 if it's available.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
