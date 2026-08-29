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

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/edsrzf/mmap-go) = %{version}

Requires:       go(golang.org/x/sys)

%description
mmap-go provides a portable memory-mapped file package for Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
