# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zstd
%define go_import_path  github.com/DataDog/zstd

Name:           go-github-datadog-zstd
Version:        1.5.7
Release:        %autorelease
Summary:        Zstd wrapper for Go
License:        BSD-3-Clause
URL:            https://github.com/DataDog/zstd
#!RemoteAsset:  sha256:17b03dcb1da22926a24676b41bc3d2951fa16b2ecbcfac89db8797b9108115ac
Source0:        https://github.com/DataDog/zstd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/DataDog/zstd) = %{version}

%description
Zstd Go Wrapper

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
