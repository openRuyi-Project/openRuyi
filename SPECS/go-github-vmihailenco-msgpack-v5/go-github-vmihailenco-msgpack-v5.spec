# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           msgpack
%define go_import_path  github.com/vmihailenco/msgpack/v5

Name:           go-github-vmihailenco-msgpack-v5
Version:        5.4.1
Release:        %autorelease
Summary:        msgpack.org[Go] MessagePack encoding for Golang
License:        BSD-2-Clause
URL:            https://github.com/vmihailenco/msgpack
#!RemoteAsset:  sha256:cffb190f68ddf9d248e1587080466981ed911cf08901c6a81f4edc8d66b69f90
Source0:        https://github.com/vmihailenco/msgpack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/vmihailenco/tagparser/v2)
BuildRequires:  go(google.golang.org/appengine)

Provides:       go(github.com/vmihailenco/msgpack/v5) = %{version}

Requires:       go(github.com/vmihailenco/tagparser/v2)
Requires:       go(google.golang.org/appengine)

%description
MessagePack encoding for Golang

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
