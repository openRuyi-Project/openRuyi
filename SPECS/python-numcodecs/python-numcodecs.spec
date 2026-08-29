# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname numcodecs

Name:           python-%{srcname}
Version:        0.16.5
Release:        %autorelease
Summary:        Buffer compression and transformation codecs
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
#!RemoteAsset:  sha256:0d0fb60852f84c0bd9543cc4d2ab9eefd37fc8efcc410acd4777e62a1d300318
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l numcodecs
# No module named 'zarr' (circular dependency)
BuildOption(check):  -e 'numcodecs.zarr3'
# No module named 'zarr' (circular dependency)
BuildOption(check):  -e 'numcodecs.tests.test_zarr3'
# No module named 'pcodec'
BuildOption(check):  -e 'numcodecs.pcodec'
BuildOption(check):  -e 'numcodecs.tests.test_pcodec'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(google-crc32c)
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(py-cpuinfo)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyzstd)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(zfpy)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Numcodecs provides buffer compression and transformation codecs for use
in data storage and communication applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
