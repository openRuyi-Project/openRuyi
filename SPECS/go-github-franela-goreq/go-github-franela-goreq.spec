# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goreq
%define go_import_path  github.com/franela/goreq
%define commit_id       bcd34c9993f899273c74baaa95e15386cd97b6e7

Name:           go-github-franela-goreq
Version:        0+git20260818.bcd34c9
Release:        %autorelease
Summary:        Simple HTTP request library for Go
License:        MIT
URL:            https://github.com/franela/goreq
#!RemoteAsset:  sha256:30539ad96348d0f9373e5b027d5b0f67de18cec51a3b04686f3056b9cb5262d4
Source0:        https://github.com/franela/goreq/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Avoid the Assertion symbol collision between the Goblin and Gomega test
# helpers while retaining the complete test suite.
Patch2000:      2000-tests-avoid-conflicting-dot-imports.patch
# Qualify the second Goblin constructor used by the parameter tests.
Patch2001:      2001-tests-qualify-the-second-Goblin-call.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/franela/goblin)
BuildRequires:  go(github.com/onsi/gomega)

Provides:       go(%{go_import_path}) = %{version}

%description
GoReq provides a simple HTTP request API built on the Go standard library.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
