# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ps
%define go_import_path  github.com/lann/ps

Name:           go-github-lann-ps
Version:        0+git20150810.62de8c4
Release:        %autorelease
Summary:        Fully persistent data structures
License:        MIT
URL:            https://github.com/lann/ps
VCS:            git:https://github.com/lann/ps.git
#!RemoteAsset:  sha256:1d0df31d2532d3f5a5292b6229310ae6ba57b9a0b8756bbbd480767dfb7d8678
Source0:        https://github.com/lann/ps/archive/62de8c46ede0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ps-62de8c46ede02a7675c4c79c84883eb164cb71e3

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lann/ps) = %{version}

%description
This package provides the github.com/lann/ps Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
