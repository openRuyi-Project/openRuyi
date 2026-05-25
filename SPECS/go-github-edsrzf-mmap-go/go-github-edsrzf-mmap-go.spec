# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mmap-go
%define go_import_path  github.com/edsrzf/mmap-go

Name:           go-github-edsrzf-mmap-go
Version:        1.2.0
Release:        %autorelease
Summary:        A portable mmap package for Go
License:        BSD-3-Clause
URL:            https://github.com/edsrzf/mmap-go
#!RemoteAsset:  sha256:9e92e9a7daeac05b86e15a5cf301767dad5a47648a33e05527911ccfa055d244
Source0:        https://github.com/edsrzf/mmap-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n mmap-go-1.2.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/edsrzf/mmap-go) = %{version}

Requires:       go(golang.org/x/sys)


%description
mmap-go

[Image: Build Status] (https://github.com/edsrzf/mmap-
go/actions/workflows/build-test.yml/badge.svg) [Image: Go Reference]
(https://pkg.go.dev/badge/github.com/edsrzf/mmap-go.svg)
(https://pkg.go.dev/github.com/edsrzf/mmap-go)

mmap-go is a portable mmap package for the Go programming language
(http://golang.org).

Operating System Support

This package is tested using GitHub Actions on Linux, macOS, and
Windows. It should also work on other Unix-like platforms, but hasn't
been tested with them. I'm interested to hear about the results.

This package compiles for Plan 9 and WebAssembly, but its functions
always return errors.

Related functions such as mprotect and mincore aren't included. I
haven't found a way to implement them on Windows without introducing
significant complexity. If you're running on a Unix-like platform and
really need these features, it should still be possible to implement
them on top of this package via syscall.


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
