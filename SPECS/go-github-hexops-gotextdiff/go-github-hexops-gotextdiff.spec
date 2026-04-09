# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotextdiff
%define go_import_path  github.com/hexops/gotextdiff

Name:           go-github-hexops-gotextdiff
Version:        1.0.3
Release:        %autorelease
Summary:        Unified text diffing in Go (copy of the internal diffing packages the officlal Go language server uses)
License:        BSD-3-Clause
URL:            https://github.com/hexops/gotextdiff
#!RemoteAsset
Source0:        https://github.com/hexops/gotextdiff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hexops/gotextdiff) = %{version}

%description
gotextdiff - unified text diffing in Go

This is a copy of the Go text diffing packages that the official Go
language server gopls uses internally
(https://github.com/golang/tools/tree/master/internal/lsp/diff) to
generate unified diffs.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
