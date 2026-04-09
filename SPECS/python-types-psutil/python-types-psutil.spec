# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types_psutil
%global pypi_name types-psutil
%global install_name psutil-stubs

Name:           python-%{pypi_name}
Version:        7.2.2.20260130
Release:        %autorelease
Summary:        Typing stubs for psutil
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{install_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Typeshed contains external type annotations for the Python standard library and Python builtins, as well as third-party packages that are contributed by people external to those projects.

%check
# This is a type stubs package, there are no runtime modules to import and check.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
