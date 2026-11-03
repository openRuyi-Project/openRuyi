# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname defcon

Name:           python-%{srcname}
Version:        0.12.2
Release:        %autorelease
Summary:        A set of flexible objects for representing UFO data
License:        MIT
URL:            https://github.com/robotools/defcon
#!RemoteAsset:  sha256:25dfe7fd0152ccf292cb190d1928a47d588899c20b046854293e039e1c93e5e0
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Defcon provides Python objects for reading, editing, and writing fonts in the
Unified Font Object format.

%pyproject_extras_subpkg -n python-%{srcname} lxml pens

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise the upstream font object model and glyph operations.
%{python3} -m unittest discover -s Lib/defcon/test -t Lib

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
