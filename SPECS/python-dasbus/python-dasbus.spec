# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dasbus

Name:           python-%{srcname}
Version:        1.7
Release:        %autorelease
Summary:        DBus library in Python
License:        LGPL-2.1-or-later
URL:            https://github.com/rhinstaller/dasbus
#!RemoteAsset:  sha256:a8850d841adfe8ee5f7bb9f82cf449ab9b4950dc0633897071718e0d0036b6f6
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Dasbus is a DBus library written in Python, based on
GLib and inspired by pydbus. It is designed to be easy
to use and extend.

%generate_buildrequires
%pyproject_buildrequires

# No check for this package
%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
