# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools_gettext

Name:           python-setuptools-gettext
Version:        0.1.14
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/setuptools-gettext
Summary:        Setuptools plugin for gettext
Provides:       python3-setuptools-gettext
%python_provide python3-setuptools-gettext
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pytest
BuildRequires:  gettext
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
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
