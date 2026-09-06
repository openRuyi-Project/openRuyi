# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotest.tools
%define go_import_path  gotest.tools

Name:           go-gotest-tools
Version:        2.3.0
Release:        %autorelease
Summary:        Go packages supporting common test patterns
License:        Apache-2.0
URL:            https://github.com/gotestyourself/gotest.tools
#!RemoteAsset:  sha256:4127bdf4ecd371783f87bf3c229b0b3b15965eb69f965c698311e69b30250649
Source0:        https://github.com/gotestyourself/gotest.tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport upstream compatibility fixes for current Go and go-cmp.
Patch1:         0001-tests-support-current-Go-and-dependencies.patch
# Use a local listener because OBS builds have no external network access.
Patch2000:      2000-poll-use-a-local-listener-in-connection-test.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(gotest.tools/assert) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/tools)

%description
Gotest.tools provides assertions, polling, filesystem fixtures, command
execution helpers, and other utilities for Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
