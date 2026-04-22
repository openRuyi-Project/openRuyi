# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname idna

Name:           python-%{srcname}
Version:        3.10
Release:        %autorelease
Summary:        Internationalized domain names in applications
License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
#!RemoteAsset:  sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891.  This version of the
protocol is often referred to as “IDNA2008” and can produce different results
from the earlier standard from 2003.  The library is also intended to act as a
suitable drop-in replacement for the “encodings.idna” module that comes with
the Python standard library but currently only supports the older 2003
specification.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.md
%doc README*

%changelog
%autochangelog
