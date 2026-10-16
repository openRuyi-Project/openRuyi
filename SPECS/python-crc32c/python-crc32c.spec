# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname crc32c

Name:           python-%{srcname}
Version:        2.8
Release:        %autorelease
Summary:        Hardware-accelerated CRC32C implementation for Python
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/ICRAR/crc32c
#!RemoteAsset:  sha256:578728964e59c47c356aeeedee6220e021e124b9d3e8631d95d9a5e5f06e261c
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  gcc
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools) >= 61

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Crc32c provides a hardware-accelerated Python implementation of the CRC32C
checksum algorithm with a portable fallback.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst AUTHORS.google-crc32c
%license LICENSE LICENSE.google-crc32c LICENSE.slice-by-8

%changelog
%autochangelog
