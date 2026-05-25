# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tomb.v1
%define go_import_path  gopkg.in/tomb.v1
%define commit_id dd632973f1e7218eb1089048e0798ec9ae7dceb8

Name:           go-gopkg-tomb.v1
Version:        0+git20260602.dd63297
Release:        %autorelease
Summary:        Tomb helps with clean goroutine termination in Go
License:        BSD-3-Clause
URL:            https://github.com/go-tomb/tomb
#!RemoteAsset:  sha256:c5fa1f3b2c687c6157507fe62a1e0aff50d0ca974138c98ded8160bea39fb06c
Source0:        https://github.com/go-tomb/tomb/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-killf-test-format-string.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/tomb.v1) = %{version}

%description
The tomb package helps with clean goroutine termination in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
