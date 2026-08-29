# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cron-converter
%global pypi_name cron_converter

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Cron string parser and scheduler for Python
License:        MIT
URL:            https://github.com/Sonic0/cron-converter
#!RemoteAsset:  sha256:53eb26be3eb2e0f206a6e227ca0c19b3807b44a24b39f4eda3718703e6474f4a
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Cron-converter provides a Cron string parser (from string/lists to string/lists)
and iteration for the datetime object with a cron like format.This project would
be a transposition in Python of JS cron-converter by roccivic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
