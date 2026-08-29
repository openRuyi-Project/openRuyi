# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname alabaster

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Configurable sidebar-enabled Sphinx theme
License:        BSD-3-Clause
URL:            https://alabaster.readthedocs.io/
VCS:            git:https://github.com/sphinx-doc/alabaster.git
#!RemoteAsset:  sha256:c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
# No module named 'pygments'
BuildOption(check):  -e %{srcname}.support

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Alabaster is a configurable sidebar-enabled Sphinx theme.  It is the
default theme for Sphinx-based documentation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
