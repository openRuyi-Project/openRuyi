# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastrand
%define go_import_path  github.com/valyala/fastrand

Name:           go-github-valyala-fastrand
Version:        1.1.0
Release:        %autorelease
Summary:        Fast pseudorandom number generator for Go
License:        MIT
URL:            https://github.com/valyala/fastrand
#!RemoteAsset:  sha256:04b51f8e3f3ddbc940e01a92f34376709a6722f43918bcf3b3369b302ee68d1d
Source0:        https://github.com/valyala/fastrand/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/valyala/fastrand) = %{version}

%description
Fastrand provides fast pseudorandom number generators that scale across
multiple CPUs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
