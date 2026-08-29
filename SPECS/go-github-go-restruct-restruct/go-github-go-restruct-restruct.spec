# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           restruct
%define go_import_path  github.com/go-restruct/restruct

Name:           go-github-go-restruct-restruct
Version:        1.2.0~alpha
Release:        %autorelease
Summary:        Implements packing and unpacking of raw binary formats
License:        ISC
URL:            https://github.com/go-restruct/restruct
#!RemoteAsset:  sha256:0bbeb53a7da45327204fe824b3d319b30b85c32e04bdb18c8bb4cb8ffafdfc31
Source0:        https://github.com/go-restruct/restruct/archive/v1.2.0-alpha.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/go-restruct/restruct) = %{version}

Requires:       go(github.com/pkg/errors)

%description
restruct is a library for reading and writing binary data in Go. Similar
to lunixbochs struc and encoding/binary, this library reads data based
on the layout of structures and, like struc, based on what is contained
in struct tags.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
