# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang-asm
%define go_import_path  github.com/twitchyliquid64/golang-asm

Name:           go-github-twitchyliquid64-golang-asm
Version:        0.15.1
Release:        %autorelease
Summary:        Standalone Go assembler library
License:        BSD-3-Clause
URL:            https://github.com/twitchyliquid64/golang-asm
#!RemoteAsset:  sha256:8954a1cf395981ecdca9b09984d2d156e90bfdfb7131fe1f68aa48f70f279cd0
Source0:        https://github.com/twitchyliquid64/golang-asm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream non-constant and recursive format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/twitchyliquid64/golang-asm) = %{version}

%description
Golang-asm is a standalone library built from the Go compiler assembler with
rewritten import paths. It exposes the assembler for use by other Go programs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
