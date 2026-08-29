# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyserial

Name:           python-%{srcname}
Version:        3.5
Release:        %autorelease
Summary:        Python serial port access library
License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/pyserial
#!RemoteAsset:  sha256:3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l serial
# skip some tests we don't need to run
BuildOption(check):  -e serial.serialwin32 -e serial.win32 -e serial.tools.list_ports_windows
BuildOption(check):  -e serial.tools.list_ports_osx
BuildOption(check):  -e serial.serialjava
BuildOption(check):  -e serial.serialcli
BuildOption(check):  -e serial.urlhandler.protocol_cp2110

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module encapsulates the access for the serial port. It provides backends
for standard Python running on Windows, Linux, BSD (possibly any POSIX
compliant system) and Jython. The module named "serial" automatically selects
the appropriate backend.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc LICENSE.txt CHANGES.rst README.rst examples
%{_bindir}/pyserial-miniterm
%{_bindir}/pyserial-ports

%changelog
%autochangelog
