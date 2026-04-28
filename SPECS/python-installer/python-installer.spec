# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname installer

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        Installer library for Python wheels
License:        MIT
URL:            https://installer.rtfd.io/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pytest

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This package provides a low-level library for installing a Python
package from a wheel distribution.  It provides basic functionality and
abstractions for handling wheels and installing packages from wheels.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest

%files -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTING.md README.md

%changelog
%{?autochangelog}
