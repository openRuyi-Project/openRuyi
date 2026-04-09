# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname asgiref

Name:           python-%{srcname}
Version:        3.8.1
Release:        %autorelease
# bundled async-timeout is Apache-2.0
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/django/asgiref/
Summary:        ASGI specs, helper code, and adapters
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto

# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
# This code is modified and probably cannot be unvendored.
Provides:       bundled(python3dist(async-timeout)) == 3.0.1

%description
ASGI is a standard for Python asynchronous web apps and servers to
communicate with each other, and positioned as an asynchronous successor to
WSGI.  This package includes libraries for implementing ASGI servers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
