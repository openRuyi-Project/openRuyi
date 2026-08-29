# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-shellwords
%define go_import_path  github.com/mattn/go-shellwords

Name:           go-github-mattn-go-shellwords
Version:        1.0.14
Release:        %autorelease
Summary:        Parse line as shell words
License:        MIT
URL:            https://github.com/mattn/go-shellwords
#!RemoteAsset:  sha256:8321ef5121866ce370f5d6af7bc4182754a3758125f266febe00b1c88022d3c4
Source0:        https://github.com/mattn/go-shellwords/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream tests use dynamic strings with t.Fatalf, rejected by current go vet.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mattn/go-shellwords) = %{version}

%description
Parse line as shell words.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
