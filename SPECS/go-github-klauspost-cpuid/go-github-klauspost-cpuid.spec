# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cpuid
%define go_import_path  github.com/klauspost/cpuid

Name:           go-github-klauspost-cpuid
Version:        1.3.1
Release:        %autorelease
Summary:        CPU feature detection for Go
License:        MIT
URL:            https://github.com/klauspost/cpuid
#!RemoteAsset:  sha256:3bf2da7358c8ed33c05bac2ca733749ade03eadf184d81cc7b16fcbe2e230f1d
Source0:        https://github.com/klauspost/cpuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/cpuid) = %{version}

%description
CPU feature detection for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
