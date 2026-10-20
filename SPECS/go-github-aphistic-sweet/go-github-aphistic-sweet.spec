# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sweet
%define go_import_path  github.com/aphistic/sweet
# failtests intentionally returns failure and is exercised by TestFailureReturnCode.
%define go_test_exclude %{go_import_path}/failtests

Name:           go-github-aphistic-sweet
Version:        0.3.0
Release:        %autorelease
Summary:        Pluggable test runner for Go
License:        MIT
URL:            https://github.com/aphistic/sweet
#!RemoteAsset:  sha256:bbc952e6ac05ba172eb1605b91598ac0ef4c8a0addf7b368abed5bfb4c46d8f1
Source0:        https://github.com/aphistic/sweet/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The runner rejects current Go testing.MainStart signatures and fails go vet.
Patch2000:      2000-support-modern-go-testing.patch
# go-diff 1.4 changes ANSI reset boundaries in the string diff fixture.
Patch2001:      2001-refresh-string-diff-fixture.patch

BuildOption(prep):  -n sweet-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mgutz/ansi)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/aphistic/sweet) = %{version}

Requires:       go(github.com/mgutz/ansi)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(golang.org/x/crypto)

%description
Sweet provides test suites and a pluggable runner integrated with the
standard Go testing package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
