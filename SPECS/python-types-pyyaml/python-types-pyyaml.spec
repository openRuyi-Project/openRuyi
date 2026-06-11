# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname types-pyyaml
%global pypi_name types_pyyaml

Name:           python-%{srcname}
Version:        6.0.12.20260518
Release:        %autorelease
Summary:        Typing stubs for PyYAML
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:d917f83fb38462550338c1297faedd860b3ec83912b96b1e3d73255f7473e466
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  yaml-stubs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
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
