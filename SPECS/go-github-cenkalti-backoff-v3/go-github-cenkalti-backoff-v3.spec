# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backoff
%define go_import_path  github.com/cenkalti/backoff/v3

Name:           go-github-cenkalti-backoff-v3
Version:        3.2.2
Release:        %autorelease
Summary:        Implements backoff algorithms for retrying operations
License:        MIT
URL:            https://github.com/cenkalti/backoff
#!RemoteAsset:  sha256:9c059d5a828343241d4daae38b8aa2bdb4f5d6b31f2aaf9d57892f3b422c3fa4
Source0:        https://github.com/cenkalti/backoff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Associate the context example with the existing Retry API for Go vet.
Patch2000:      2000-fix-context-example-name.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cenkalti/backoff/v3) = %{version}

%description
Backoff provides exponential retry delays, configurable retry policies,
and context-aware cancellation for Go applications using the v3 API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
