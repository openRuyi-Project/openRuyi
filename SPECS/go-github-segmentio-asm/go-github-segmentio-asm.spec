# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           asm
%define go_import_path  github.com/segmentio/asm
# build/* packages are generator helpers and fail with the current cpu feature API;
# runtime packages such as base64/keyset are still tested. - HNO3Miracle
%define go_test_exclude_glob github.com/segmentio/asm/build*

Name:           go-github-segmentio-asm
Version:        1.2.1
Release:        %autorelease
Summary:        Go library providing algorithms that use modern CPU features
License:        MIT-0
URL:            https://github.com/segmentio/asm
#!RemoteAsset:  sha256:47bd144ee60642b19a0118143005038e4ce5009f8e90e3ec168a257099ac887d
Source0:        https://github.com/segmentio/asm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mmcloughlin/avo)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/segmentio/asm) = %{version}

Requires:       go(github.com/mmcloughlin/avo)
Requires:       go(golang.org/x/sys)

%description
asm provides Go implementations of performance-sensitive algorithms optimized
to use modern CPU features and instruction sets.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
