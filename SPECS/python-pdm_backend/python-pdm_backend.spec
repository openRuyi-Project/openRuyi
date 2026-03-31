# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pdm_backend

Name:           python-%{srcname}
Version:        2.4.3
Release:        %autorelease
License:        MIT
URL:            https://pdm-backend.fming.dev/
Summary:        PEP 517 build backend for PDM
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pdm +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
PDM-Backend is a build backend that supports the latest packaging
standards, which includes PEP 517, PEP 621 and PEP 660.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE
%changelog
%{?autochangelog}
