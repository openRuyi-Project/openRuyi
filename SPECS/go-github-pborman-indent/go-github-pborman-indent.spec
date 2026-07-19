# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           indent
%define go_import_path  github.com/pborman/indent

Name:           go-github-pborman-indent
Version:        1.2.1
Release:        %autorelease
Summary:        Indents lines of text with a prefix
License:        Apache-2.0
URL:            https://github.com/pborman/indent
#!RemoteAsset:  sha256:43b269bb6ac28a00570db0dd2018775ad78eaf26f1313114e96f83fee4739aff
Source0:        https://github.com/pborman/indent/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pborman/indent) = %{version}

%description
The indent package indents lines of text with a prefix.  It supports
indent blocks of text (string or []byte) as well as providing an
io.Writer interface. It is a drop-in replacement for the
github.com/openconfig/goyang/pkg/indent package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
