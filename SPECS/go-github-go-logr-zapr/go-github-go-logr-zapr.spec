# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zapr
%define go_import_path  github.com/go-logr/zapr

Name:           go-github-go-logr-zapr
Version:        1.3.0
Release:        %autorelease
Summary:        logr implementation built on Zap
License:        Apache-2.0
URL:            https://github.com/go-logr/zapr
#!RemoteAsset:  sha256:37a516aa30dd42af8be6edd8ab8ba3684b197374f763f0655078bfe9fb2e44cc
Source0:        https://github.com/go-logr/zapr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 slogtest rejects empty nested groups
BuildOption(check):  -skip TestSlogHandler

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/multierr)

Provides:       go(github.com/go-logr/zapr) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(go.uber.org/zap)

%description
A logr implementation using Zap. It can also be used as a slog handler.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
