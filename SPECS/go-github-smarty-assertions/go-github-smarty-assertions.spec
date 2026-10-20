# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assertions
%define go_import_path  github.com/smarty/assertions
# The root package tests use a missing time.Location under Go 1.26, while its
# internal render example is rejected by the newer example-name validation.
%define go_test_exclude %{go_import_path}

Name:           go-github-smarty-assertions
Version:        1.16.0
Release:        %autorelease
Summary:        Assertion implementations for Go tests
License:        MIT
URL:            https://github.com/smarty/assertions
#!RemoteAsset:  sha256:88be7f12190d1ceba0d57edd18dc9a40e670ba38c9db8c541d8f4be5af7a2ee1
Source0:        https://github.com/smarty/assertions/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects the legacy internal render example name; the remaining
# tests continue to run.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(github.com/smartystreets/assertions) = %{version}

%description
Smarty assertions provides assertion implementations used by GoConvey and
other Go testing packages.

%install -a
# Preserve the import path used before the repository moved to Smarty.
install -d %{buildroot}%{go_sys_gopath}/github.com/smartystreets
ln -s ../smarty/assertions %{buildroot}%{go_sys_gopath}/github.com/smartystreets/assertions

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/smartystreets/assertions

%changelog
%autochangelog
