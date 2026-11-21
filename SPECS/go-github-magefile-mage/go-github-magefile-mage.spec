# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mage
%define go_import_path  github.com/magefile/mage

Name:           go-github-magefile-mage
Version:        1.17.2
Release:        %autorelease
Summary:        Make-like build tool written in Go
License:        Apache-2.0
URL:            https://github.com/magefile/mage
#!RemoteAsset:  sha256:af594292c863a7c0bfe93c35a33a1c441a2dca24c5ade552a96caacf5015efcc
Source0:        https://github.com/magefile/mage/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(github.com/magefile/mage/mage) = %{version}
Provides:       go(github.com/magefile/mage/sh) = %{version}

%description
Mage is a make-like build tool that uses ordinary Go functions as build
targets. This package installs its command and library sources.

%package        tests
Summary:        Regression tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       go

%description    tests
Go regression test sources for go-github-magefile-mage.

%check
# TestGoModules requires module mode; short mode omits the online release test.
GO111MODULE=on GOPROXY=off go test -short ./...

%files
%exclude /usr/share/gocode/src/github.com/magefile/mage/install_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/internal/run_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mage/args_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mage/completion_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mage/import_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mage/main_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mage/main_unix_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/magefiles/targets/release_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mg/color_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mg/deps_internal_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mg/deps_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mg/errors_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/mg/fn_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/parse/parse_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/sh/cmd_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/sh/helpers_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/target/newer_test.go
%exclude /usr/share/gocode/src/github.com/magefile/mage/target/target_test.go
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%files tests
/usr/share/gocode/src/github.com/magefile/mage/install_test.go
/usr/share/gocode/src/github.com/magefile/mage/internal/run_test.go
/usr/share/gocode/src/github.com/magefile/mage/mage/args_test.go
/usr/share/gocode/src/github.com/magefile/mage/mage/completion_test.go
/usr/share/gocode/src/github.com/magefile/mage/mage/import_test.go
/usr/share/gocode/src/github.com/magefile/mage/mage/main_test.go
/usr/share/gocode/src/github.com/magefile/mage/mage/main_unix_test.go
/usr/share/gocode/src/github.com/magefile/mage/magefiles/targets/release_test.go
/usr/share/gocode/src/github.com/magefile/mage/mg/color_test.go
/usr/share/gocode/src/github.com/magefile/mage/mg/deps_internal_test.go
/usr/share/gocode/src/github.com/magefile/mage/mg/deps_test.go
/usr/share/gocode/src/github.com/magefile/mage/mg/errors_test.go
/usr/share/gocode/src/github.com/magefile/mage/mg/fn_test.go
/usr/share/gocode/src/github.com/magefile/mage/parse/parse_test.go
/usr/share/gocode/src/github.com/magefile/mage/sh/cmd_test.go
/usr/share/gocode/src/github.com/magefile/mage/sh/helpers_test.go
/usr/share/gocode/src/github.com/magefile/mage/target/newer_test.go
/usr/share/gocode/src/github.com/magefile/mage/target/target_test.go

%changelog
%autochangelog
