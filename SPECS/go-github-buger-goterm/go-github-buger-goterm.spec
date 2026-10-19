# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goterm
%define go_import_path  github.com/buger/goterm
# Each example is a standalone main program, not part of one Go package.
%define go_test_exclude_glob  %{go_import_path}/examples

Name:           go-github-buger-goterm
Version:        1.0.4
Release:        %autorelease
Summary:        Building blocks for terminal user interfaces in Go
License:        MIT
URL:            https://github.com/buger/goterm
#!RemoteAsset:  sha256:9fd8bc9480373eb01706f81f9402887d22a3afd269a7a77e1d85fbe8d6f600af
Source0:        https://github.com/buger/goterm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Goterm provides terminal cursor control, colors, boxes, tables, and charts
for building console interfaces.

%check -a
# Compile examples separately without running their interactive event loops.
for example in examples/*.go; do
    go test "$example"
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
