# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hydra-core
%global pypi_name hydra_core

Name:           python-%{srcname}
Version:        1.3.7
Release:        %autorelease
Summary:        A framework for elegantly configuring complex applications
License:        MIT
URL:            https://github.com/facebookresearch/hydra
#!RemoteAsset:  sha256:d4ff629c7e23b64a9db5fe5b027cf7c55b633b737f03be51ef41b77ed016f75e
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
