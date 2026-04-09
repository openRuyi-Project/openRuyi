# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zap
%define go_import_path  go.uber.org/zap
# Tests fail due to benchmark
%define go_test_ignore_failure 1

Name:           go-uber-zap
Version:        1.27.1
Release:        %autorelease
Summary:        Blazing fast, structured, leveled logging in Go.
License:        MIT
URL:            https://github.com/uber-go/zap
#!RemoteAsset
Source0:        https://github.com/uber-go/zap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(go.uber.org/zap) = %{version}

%description
Package zap provides fast, structured, leveled logging.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
