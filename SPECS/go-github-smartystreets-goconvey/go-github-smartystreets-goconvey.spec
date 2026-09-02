# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goconvey
%define go_import_path  github.com/smartystreets/goconvey
# The root fixture has an unstable time comparison, and the watcher test relies
# on filesystem notification timing that is not deterministic in OBS.
%define go_test_exclude %{go_import_path} %{go_import_path}/web/server/watch

Name:           go-github-smartystreets-goconvey
Version:        1.8.1
Release:        %autorelease
Summary:        BDD-style testing framework for Go
License:        MIT
URL:            https://github.com/smartystreets/goconvey
#!RemoteAsset:  sha256:d51d934afee3e2306881439028dd4115167d261b5e4de5a930897fefe2e5b8a3
Source0:        https://github.com/smartystreets/goconvey/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Count only goroutine stack headers with Go 1.26 stack output.
Patch2000:      2000-convey-count-only-goroutine-stack-headers.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jtolds/gls)
BuildRequires:  go(github.com/smarty/assertions)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/jtolds/gls)
Requires:       go(github.com/smarty/assertions)
Requires:       go(golang.org/x/tools)

%description
GoConvey provides BDD-style assertions and test execution helpers for Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
