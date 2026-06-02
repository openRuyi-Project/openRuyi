# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname icalendar

Name:           python-%{srcname}
Version:        7.1.0
Release:        %autorelease
Summary:        RFC 5545 compatible parser and generator of iCalendar files
License:        BSD-2-Clause
URL:            https://icalendar.readthedocs.io
VCS:            git:https://github.com/collective/icalendar.git
#!RemoteAsset:  sha256:10cd223c792fcc43bee4c3ebe3149d4cf32406c85cfef146624df5a0d414260f
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(tzdata)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
icalendar is a parser and generator of RFC 5545 compatible iCalendar
files for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst
%{_bindir}/icalendar

%changelog
%autochangelog
