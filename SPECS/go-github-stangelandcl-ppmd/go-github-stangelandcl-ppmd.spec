# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ppmd
%define go_import_path  github.com/stangelandcl/ppmd

Name:           go-github-stangelandcl-ppmd
Version:        0.1.1
Release:        %autorelease
Summary:        PPMD variant H with 7-zip extensions decompressor for go
License:        MIT
URL:            https://github.com/stangelandcl/ppmd
#!RemoteAsset:  sha256:718002d09007f18ba1ba0ff99058fd71a294b797cd30dca42643a59b03e9094d
Source0:        https://github.com/stangelandcl/ppmd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/stangelandcl/ppmd) = %{version}

%description
PPMD variant H with 7-zip extensions decompressor for go.

PPMD7 in 7-zip source code.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
