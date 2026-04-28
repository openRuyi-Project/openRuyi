# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname time-machine
%global modname time_machine

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Travel through time in your Python tests
License:        MIT
URL:            https://time-machine.readthedocs.io/en/latest/
VCS:            git:https://github.com/adamchainz/time-machine
#!RemoteAsset:  sha256:a4ddd1cea17b8950e462d1805a42b20c81eb9aafc8f66b392dd5ce997e037d79
Source0:        https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tokenize-rt)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python library that allows to travel in time and freeze it as well.
Includes a test-function decorator that sets time to an arbitrary value.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{python3_sitearch}/time_machine/
%{python3_sitearch}/_time_machine.*.so
%{python3_sitearch}/time_machine-%{version}.dist-info/

%changelog
%autochangelog
