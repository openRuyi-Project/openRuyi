# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpgzip
%define go_import_path  github.com/shurcooL/httpgzip
%define commit_id d1585fc322fa7cad2956ba8e01a41a39d09d6b31

Name:           go-github-shurcool-httpgzip
Version:        0+git20260607.d1585fc
Release:        %autorelease
Summary:        Gzip-enabled net/http primitives for Go
License:        MIT
URL:            https://github.com/shurcooL/httpgzip
#!RemoteAsset:  sha256:71f30f4c752880fc5746024af93d73c5d82f016322850a572391e6d2f35b0045
Source0:        https://github.com/shurcooL/httpgzip/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstreamable test fixture modernization: replace obsolete x/tools godoc VFS
# fixtures with standard-library filesystem fixtures.
# - HNO3Miracle
Patch0:         0001-drop-x-tools-test-deps.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/shurcooL/httpgzip) = %{version}

Requires:       go(golang.org/x/net)

%description
Package httpgzip provides net/http-like primitives that use gzip compression
when serving HTTP requests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
