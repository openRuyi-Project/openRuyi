# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kai Zhang <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyQt6-sip
%global pypi_name pyqt6_sip

Name:           python-pyqt6-sip
Version:        13.11.1
Release:        %autorelease
Summary:        The sip module support for PyQt6
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/sip/
#!RemoteAsset:  sha256:869c5b48afe38e55b1ee0dd72182b0886e968cc509b98023ff50010b013ce1be
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l PyQt6

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pyqt6-sip = %{version}-%{release}
Provides:       python3-pyqt6-sip%{?_isa} = %{version}-%{release}
%python_provide python3-pyqt6-sip

%description
The sip extension module provides support for the PyQt6 package.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README

%changelog
%autochangelog
