# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hydra-core
%global pypi_name hydra_core

Name:           python-%{srcname}
Version:        1.3.8
Release:        %autorelease
Summary:        A framework for elegantly configuring complex applications
License:        MIT
URL:            https://github.com/facebookresearch/hydra
#!RemoteAsset:  sha256:18d5dfb841734a936507e75e7b8390b406ed22494f7fb8b4b7b7c122102de3d5
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hydra

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  java-latest-openjdk

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Hydra is a framework for elegantly configuring complex applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
