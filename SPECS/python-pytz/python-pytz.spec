# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytz

Name:           python-%{srcname}
Version:        2025.1
Release:        %autorelease
Summary:        Python timezone library
License:        MIT
URL:            http://pythonhosted.org/pytz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  tzdata
Requires:       tzdata
BuildSystem:    pyproject
BuildOption(install):  -l %{srcname} +auto

%description
This library brings the Olson tz database into Python.  It
allows accurate and cross platform timezone calculations using Python 2.4 or
higher.  It also solves the issue of ambiguous times at the end of daylight
saving time.  Almost all of the Olson timezones are supported.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README*
%changelog
%autochangelog
