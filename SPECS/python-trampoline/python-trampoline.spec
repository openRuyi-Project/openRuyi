# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname trampoline
%global commit 1d98f39c3015594e2ac8ed48dccc2f393b4dd82b

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Generator-based coroutines for Python
License:        MIT
URL:            https://gitlab.com/ferreum/trampoline
#!RemoteAsset:  sha256:4e026488a57a7a49b3c4a809a93ace8fcccae5b66a7ef9b1b9581755c38ae15f
Source0:        https://github.com/ferreum/trampoline/archive/%{commit}/%{srcname}-%{commit}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(prep):  -n %{srcname}-%{commit}
BuildOption(install):  trampoline

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Trampoline provides cooperative scheduling of generator-based coroutines.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
