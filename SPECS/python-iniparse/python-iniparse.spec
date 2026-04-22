# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname iniparse

Name:           python-%{srcname}
Version:        0.5
Release:        %autorelease
Summary:        Accessing and Modifying INI files
License:        MIT
URL:            https://github.com/candlepin/python-iniparse
#!RemoteAsset:  sha256:932e5239d526e7acb504017bb707be67019ac428a6932368e6851691093aa842
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
iniparse is an INI parser for Python which is API compatible with the standard
library’s ConfigParser, preserves structure of INI files (order of sections &
options, indentation, comments, and blank lines are preserved when data is
updated), and is more convenient to use.

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -vfr %{buildroot}%{_docdir}/*

%files -f %{pyproject_files}
%doc README.md Changelog

%changelog
%autochangelog
