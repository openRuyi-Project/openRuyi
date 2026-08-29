# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cronexpr
%define go_import_path  github.com/hashicorp/cronexpr

Name:           go-github-hashicorp-cronexpr
Version:        1.1.3
Release:        %autorelease
Summary:        Cron expression parser in Go language (golang)
License:        Apache-2.0
URL:            https://github.com/hashicorp/cronexpr
#!RemoteAsset:  sha256:1d546a0497dd21a16f75745bd5645af96d63f506249f4582855f2a9fdc07f29a
Source0:        https://github.com/hashicorp/cronexpr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
# For tests
BuildRequires:  tzdata

Provides:       go(github.com/hashicorp/cronexpr) = %{version}

%description
Golang Cron expression parser

Given a cron expression and a time stamp, you can get the next time
stamp which satisfies the cron expression.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
