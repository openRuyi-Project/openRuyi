# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           text
%define go_import_path  github.com/tenntenn/text
%define commit          ba836492e880a47581a642ca2117da5f04524f5a

Name:           go-github-tenntenn-text
Version:        1.0.0+git20261023.ba83649
Release:        %autorelease
Summary:        Streaming text replacement utilities for Go
License:        MIT
URL:            https://github.com/tenntenn/text
# The latest release lacks a license file; this snapshot includes upstream's MIT license.
#!RemoteAsset:  sha256:8bf66e31754620cf2a0a0399f81a3fbdbe6c84aeddb6a1154a7095ad35befca2
Source0:        https://github.com/tenntenn/text/archive/%{commit}.tar.gz#/%{_name}-%{commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.8
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/transform)

Provides:       go(github.com/tenntenn/text/transform) = %{version}

Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/text/transform)

%description
Streaming text replacement utilities compatible with golang.org/x/text/transform.
This package contains the complete upstream repository sources and tests.
The transform module is installed at its declared import path beneath the
repository root.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
