# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-generics-cache
%define go_import_path  github.com/Code-hex/go-generics-cache
# Test cases has case-insensitive problem, ignore test - Julian
%define go_test_ignore_failure 1

Name:           go-github-code-hex-go-generics-cache
Version:        1.5.1
Release:        %autorelease
Summary:        A key:value store/cache library written in Go generics. LRU, LFU, FIFO, MRU, Clock support.
License:        MIT
URL:            https://github.com/code-hex/go-generics-cache
#!RemoteAsset
Source0:        https://github.com/code-hex/go-generics-cache/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/code-hex/go-generics-cache) = %{version}

%description
go-generics-cache is an in-memory key:value store/cache that is suitable
for applications running on a single machine. This in-memory cache uses
Go Generics (https://go.dev/blog/generics-proposal) which is introduced
in 1.18.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
