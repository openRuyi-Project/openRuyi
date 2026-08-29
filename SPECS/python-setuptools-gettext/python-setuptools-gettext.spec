# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools-gettext
%global pypi_name setuptools_gettext

Name:           python-setuptools-gettext
Version:        0.1.14
Release:        %autorelease
Summary:        Setuptools plugin for gettext
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
#!RemoteAsset:  sha256:43f099eff31a4712cdfbcbb07e0264b0546ed3ebfd7ea998189326c519390d2c
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  gettext

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides a plugin for Setuptools for gettext.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -v -rs

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
