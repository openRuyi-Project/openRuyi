# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname interegular

Name:           python-%{srcname}
Version:        0.3.3
Release:        %autorelease
Summary:        regex intersection checker
License:        MIT
URL:            https://github.com/MegaIng/interegular
#!RemoteAsset:  sha256:d9b697b21b34884711399ba0f0376914b81899ce670032486d0d048344a76600
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A library to check a subset of python regexes for intersections.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
