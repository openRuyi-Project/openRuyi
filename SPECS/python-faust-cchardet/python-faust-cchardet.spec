# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname faust-cchardet

Name:           python-%{srcname}
Version:        2.1.19
Release:        %autorelease
Summary:        High speed universal character encoding detector
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/faust-streaming/cchardet
#!RemoteAsset:  sha256:f89386297cde0c8e0f5e21464bc2d6d0e4a4fc1b1d77cdb238ca24d740d872e0
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l cchardet

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pkgconfig)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cChardet is high speed universal character encoding detector.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/cchardetect

%changelog
%autochangelog
