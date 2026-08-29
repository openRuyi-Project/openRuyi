# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-crc32c
%global pypi_name google_crc32c

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        Python wrapper for Google CRC32C
License:        Apache-2.0
URL:            https://github.com/googleapis/python-crc32c
#!RemoteAsset:  sha256:a428e25fb7691024de47fecfbff7ff957214da51eddded0da0ae0e0f03a2cf79
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l google_crc32c

BuildRequires:  crc32c-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google CRC32C provides a Python implementation of the CRC32C checksum.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
