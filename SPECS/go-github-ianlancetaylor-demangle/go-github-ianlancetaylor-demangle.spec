# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           demangle
%define go_import_path  github.com/ianlancetaylor/demangle
# Upstream does not provide git tags, use commit ID instead - Julian
%define commit_id 96ee0021ea0fb9174681b8004d8deba3c499d7f5

Name:           go-github-ianlancetaylor-demangle
Version:        0+git20251118.96ee002
Release:        %autorelease
Summary:        C++ symbol name demangler written in Go
License:        BSD-3-Clause
URL:            https://github.com/ianlancetaylor/demangle
#!RemoteAsset
Source0:        https://github.com/ianlancetaylor/demangle/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ianlancetaylor/demangle) = %{version}

%description
A Go package that can be used to demangle C++ and Rust symbol names.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
