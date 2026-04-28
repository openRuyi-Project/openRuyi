# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname audioop-lts
%global pypi_name audioop_lts

Name:           python-%{srcname}
Version:        0.2.2
Release:        %autorelease
Summary:        An LTS port of the Python builtin module audioop for newer Python versions
License:        PSF-2.0
URL:            https://github.com/AbstractUmbra/audioop
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  audioop

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An LTS port of the Python builtin module audioop which was deprecated
since version 3.11 and removed in 3.13.

This project exists to maintain this module for future versions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
