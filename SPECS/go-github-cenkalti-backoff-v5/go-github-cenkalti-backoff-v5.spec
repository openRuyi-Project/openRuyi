# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backoff
%define go_import_path  github.com/cenkalti/backoff/v5
# The tests need too much time to run
%define go_test_exclude %{go_import_path}

Name:           go-github-cenkalti-backoff-v5
Version:        5.0.3
Release:        %autorelease
Summary:        Exponential backoff algorithm for Go
License:        MIT
URL:            https://github.com/cenkalti/backoff
#!RemoteAsset:  sha256:e967898e592ef838ca5ccfa68cf407d97adbfa757391f8942be9763646cbe3c5
Source0:        https://github.com/cenkalti/backoff/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cenkalti/backoff/v5) = %{version}

%description
Backoff implements retry operations with configurable exponential delays and
elapsed-time limits.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
