# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname freezegun

Name:           python-%{srcname}
Version:        1.5.5
Release:        %autorelease
Summary:        Test utility for mocking the datetime module
License:        Apache-2.0
URL:            https://github.com/spulec/freezegun
#!RemoteAsset:  sha256:ac7742a6cc6c25a2c35e9292dfd554b897b517d2dec26891a2e8debf205cb94a
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
