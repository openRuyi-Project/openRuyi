# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pysol-cards
%global pypi_name pysol_cards

Name:           python-%{srcname}
Version:        0.24.0
Release:        %autorelease
Summary:        Deal PySol FC Cards
License:        BSD-3-Clause
URL:            https://github.com/shlomif/pysol_cards
#!RemoteAsset:  sha256:a985492da81aa1588dfc056d9a7c6ca83f66254c0b90f25afc682a70713d4d4b
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The pysol-cards python modules allow the python developer to generate the initial deals
of some PySol FC games. It also supports PySol legacy deals and Microsoft FreeCell / Freecell Pro deals.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
