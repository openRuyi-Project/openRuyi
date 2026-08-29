# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-winio
%define go_import_path  github.com/Microsoft/go-winio

Name:           go-github-microsoft-go-winio
Version:        0.6.2
Release:        %autorelease
Summary:        Windows I/O library for Go
License:        MIT
URL:            https://github.com/Microsoft/go-winio
#!RemoteAsset:  sha256:0bf0aedbb0a38c494fda60804679e270fe98ca05dc9c2659584df1e3e1e0bd17
Source0:        https://github.com/Microsoft/go-winio/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/Microsoft/go-winio) = %{version}

%description
go-winio provides Windows I/O helpers for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
