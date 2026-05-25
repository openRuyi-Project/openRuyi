# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-findfont
%define go_import_path  github.com/flopp/go-findfont

Name:           go-github-flopp-go-findfont
Version:        0.1.0
Release:        %autorelease
Summary:        Locate TrueType font files on the host system
License:        MIT
URL:            https://github.com/flopp/go-findfont
#!RemoteAsset:  sha256:112ac63a3e2965a50f675976a88763e744bd810eb084ca8165f8e58313a925ec
Source0:        https://github.com/flopp/go-findfont/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/flopp/go-findfont) = %{version}

%description
go-findfont locates font files installed on the host system.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
