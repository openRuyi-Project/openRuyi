# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-junit
%define go_import_path  github.com/joshdk/go-junit

Name:           go-github-joshdk-go-junit
Version:        1.0.0
Release:        %autorelease
Summary:        JUnit XML parser for Go
License:        MIT
URL:            https://github.com/joshdk/go-junit
#!RemoteAsset:  sha256:9cd3692d8ed8d0f1c030304e8d22b1b1b7b8390fb93412ed60b054e6439c85b4
Source0:        https://github.com/joshdk/go-junit/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/joshdk/go-junit) = %{version}

%description
This package provides JUnit XML parser for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
