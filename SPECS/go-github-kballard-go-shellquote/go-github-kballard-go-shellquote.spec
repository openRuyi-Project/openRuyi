# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-shellquote
%define go_import_path  github.com/kballard/go-shellquote
%define commit_id       95032a82bc518f77982ea72343cc1ade730072f0

Name:           go-github-kballard-go-shellquote
Version:        0+git20260723.95032a8
Release:        %autorelease
Summary:        Shell-style word splitting and quoting utilities for Go
License:        MIT
URL:            https://github.com/kballard/go-shellquote
#!RemoteAsset:  sha256:11590ff4fcd1dc844513c03cf332e7e061165a3ab5ce28a029334e90e4a33b53
Source0:        https://github.com/kballard/go-shellquote/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kballard/go-shellquote) = %{version}

%description
go-shellquote provides Go utilities for shell-like word splitting, joining and
quoting while preserving shell escape semantics.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
