# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aioquic

Name:           python-%{srcname}
Version:        1.7.2
Release:        %autorelease
Summary:        DNS toolkit for Python
License:        BSD-3-Clause
URL:            https://github.com/aiortc/aioquic
#!RemoteAsset:  sha256:4def7cb0a692dc12c995cc397a93f41b78cc30b7bf078769c3a3bb1ba9dcf362
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname} -l

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(openssl)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A library for the QUIC network protocol in Python. It features a minimal TLS
1.3 implementation, a QUIC stack and an HTTP/3 stack.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
