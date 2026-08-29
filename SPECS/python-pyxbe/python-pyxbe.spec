# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyxbe

Name:           python-%{srcname}
Version:        1.0.3
Release:        %autorelease
Summary:        Simple construction, analysis and modification of binary data
License:        MIT
URL:            https://github.com/mborgerson/pyxbe
#!RemoteAsset:  sha256:ef38c9b07bffd9daecdd32640a3e6c99f62a621a8b8a4d54a0c2ccf9fb1b7cdb
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l xbe

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python library to read and write XBE files, the executable file format
for the original Xbox game console.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
