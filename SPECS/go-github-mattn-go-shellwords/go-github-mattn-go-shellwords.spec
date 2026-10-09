# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-shellwords
%define go_import_path  github.com/mattn/go-shellwords

Name:           go-github-mattn-go-shellwords
Version:        1.0.15
Release:        %autorelease
Summary:        Parse line as shell words
License:        MIT
URL:            https://github.com/mattn/go-shellwords
#!RemoteAsset:  sha256:eb89245b4dd6561e42ea14de96558bfba0bb05c1e8a3b3a81700a55ac91405bc
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
