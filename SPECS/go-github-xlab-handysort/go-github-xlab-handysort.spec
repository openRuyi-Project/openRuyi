# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           handysort
%define go_import_path  github.com/xlab/handysort
%define commit_id       fb3537ed64a14615a020f0fe8dc08424233d491f

Name:           go-github-xlab-handysort
Version:        0+git20260922.fb3537e
Release:        %autorelease
Summary:        Natural ordering for alphanumeric strings in Go
License:        MIT
URL:            https://github.com/xlab/handysort
#!RemoteAsset:  sha256:67c40ac3979313f81532f072b02b57bb41bfba0a28b041e2ea1babc9ae282eb4
Source0:        https://github.com/xlab/handysort/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy benchmark data generation converts integer code points to strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xlab/handysort) = %{version}

%description
Handysort compares strings by treating embedded numbers numerically
for natural alphanumeric ordering.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
