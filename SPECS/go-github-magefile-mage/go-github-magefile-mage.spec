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

%description
Mage is a make-like build tool that uses ordinary Go functions as build
targets. This package installs its command and library sources.

%check
# TestGoModules requires module mode; short mode omits the online release test.
GO111MODULE=on GOPROXY=off go test -short ./...

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
