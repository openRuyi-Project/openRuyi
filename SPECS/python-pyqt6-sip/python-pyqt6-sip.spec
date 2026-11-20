# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kai Zhang <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyQt6-sip
%global pypi_name pyqt6_sip

Name:           python-pyqt6-sip
Version:        13.13.1
Release:        %autorelease
Summary:        The sip module support for PyQt6
License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/sip/
#!RemoteAsset:  sha256:83c3c9cb93b6c631af7048084fb0f234b610a01edbf9b2b44c4ee4bda4197efe
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
