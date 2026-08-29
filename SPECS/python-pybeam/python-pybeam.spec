# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pybeam

Name:           python-%{srcname}
Version:        0.8.1
Release:        %autorelease
Summary:        Python module to parse Erlang BEAM files
License:        MIT
URL:            https://github.com/matwey/pybeam
#!RemoteAsset:  sha256:44a059cac90ba7f490c2442d561f1df6a3134fc5a0d1c2c38a3860fbcd28b0b1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
