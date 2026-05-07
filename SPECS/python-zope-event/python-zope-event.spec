# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zope-event
%global pypi_name zope_event

Name:           python-%{srcname}
Version:        6.2
Release:        %autorelease
Summary:        Very basic event publishing system
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.event
VCS:            git:https://github.com/zopefoundation/zope.event.git
#!RemoteAsset:  sha256:b97d5d6327067ee6b9dfcbdf606ade9ade70991e19c162e808ea39e5fcf0f8d3
Source:         https://files.pythonhosted.org/packages/source/z/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l zope

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The zope.event package provides a simple event system, including an event
publishing API, a very simple event-dispatching system on which more
sophisticated event dispatching systems can be built, and a way to
subscribe to events.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE.txt

%changelog
%autochangelog
