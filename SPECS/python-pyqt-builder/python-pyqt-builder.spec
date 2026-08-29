# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyQt-builder
%global pypi_name pyqt_builder

Name:           python-pyqt-builder
Version:        1.19.1
Release:        %autorelease
Summary:        The PEP 517 compliant PyQt build system
License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/pyqt/
#!RemoteAsset:  sha256:6af6646ba29668751b039bfdced51642cb510e300796b58a4d68b7f956a024d8
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# not support dynamic version.
Patch0:         0001-fix-version.patch

BuildOption(install):  -l pyqtbuild

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(sip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools-scm) >= 8

Provides:       python3-pyqt-builder = %{version}-%{release}
%python_provide python3-pyqt-builder

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules. Projects that use
PyQt-builder provide an appropriate pyproject.toml file and an optional
project.py.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel

%changelog
%autochangelog
