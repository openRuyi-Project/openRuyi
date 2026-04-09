# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname minidump

Name:           python-%{srcname}
Version:        0.0.24
Release:        %autorelease
Summary:        Python library to parse Windows minidump file format
License:        MIT
URL:            https://github.com/skelsec/minidump
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Python library to parse and read Microsoft minidump file format.
Can create minidumps on Windows machines using the windows API
(implemented with ctypes).

%prep -a
# These modules are primarily used for creating minidumps on Windows;
# they are not needed for parsing minidumps on Linux.
rm -rf minidump/utils/createminidump.py
rm -rf minidump/utils/privileges.py
rm -rf minidump/utils/winapi/
rm -rf minidump/writer.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/minidump

%changelog
%autochangelog
