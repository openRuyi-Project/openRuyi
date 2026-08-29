# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           encoding
%define go_import_path  github.com/gdamore/encoding

Name:           go-github-gdamore-encoding
Version:        1.0.1
Release:        %autorelease
Summary:        Character map encodings missing from the Go standard library
License:        Apache-2.0
URL:            https://github.com/gdamore/encoding
#!RemoteAsset:  sha256:fc14f9f1d10d60a5888536df5a08e9e0fd7dad3412b9051a370edfe4cccf538d
Source0:        https://github.com/gdamore/encoding/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/gdamore/encoding) = %{version}

Requires:       go(golang.org/x/text)

%description
Package encoding provides character encodings that are useful for dealing with
I/O streams from non-UTF friendly sources.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
