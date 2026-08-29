# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           quartz
%define go_import_path  github.com/coder/quartz

Name:           go-github-coder-quartz
Version:        0.3.1
Release:        %autorelease
Summary:        Deterministic time testing library for Go
License:        MIT-0
URL:            https://github.com/coder/quartz
#!RemoteAsset:  sha256:8456a687f16b4fd863799845b62d8092197a2a37c0c87b38c92ea78671b77978
Source0:        https://github.com/coder/quartz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/coder/quartz) = %{version}

%description
Quartz provides controllable clocks for fast, deterministic tests of time-based
Go code.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
