# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Investigate why fedora use 0.3 for anaconda, upstream already 1.5 - 251

%global srcname xkbregistry

Name:           python-%{srcname}
Version:        0.3
Release:        %autorelease
Summary:        Bindings for libxkbregistry using cffi
License:        MIT
URL:            https://github.com/sde1000/python-xkbregistry
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xkbcommon)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

Requires:       libxkbcommon

%description
Python bindings for libxkbregistry using cffi.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%{?autochangelog}
