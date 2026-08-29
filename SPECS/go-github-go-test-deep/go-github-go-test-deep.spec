# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           deep
%define go_import_path  github.com/go-test/deep

Name:           go-github-go-test-deep
Version:        1.1.1
Release:        %autorelease
Summary:        Deep variable equality helper for Go tests
License:        MIT
URL:            https://github.com/go-test/deep
#!RemoteAsset:  sha256:ed08d8f98b4620637be97602d4c9e13c0b53e2347bb21a3a0a8f85ad9919b7dd
Source0:        https://github.com/go-test/deep/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-test/deep) = %{version}

%description
deep provides a Go test helper for comparing values and reporting
human-readable differences.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
