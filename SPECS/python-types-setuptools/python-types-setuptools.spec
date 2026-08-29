# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types-setuptools
%global pypi_name types_setuptools

Name:           python-types-setuptools
Version:        80.10.0.20260124
Release:        %autorelease
Summary:        Typing stubs for setuptools
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:1b86d9f0368858663276a0cbe5fe5a9722caf94b5acde8aba0399a6e90680f20
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  setuptools-stubs distutils-stubs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-types-setuptools = %{version}-%{release}
%python_provide python3-types-setuptools

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
