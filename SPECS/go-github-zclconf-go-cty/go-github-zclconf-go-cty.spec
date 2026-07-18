# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cty
%define go_import_path  github.com/zclconf/go-cty

Name:           go-github-zclconf-go-cty
Version:        1.19.0
Release:        %autorelease
Summary:        A type system for dynamic values in Go applications
License:        MIT
URL:            https://github.com/zclconf/go-cty
#!RemoteAsset:  sha256:1fbd94656e6ca6532665229e4a3fe3b4e72083f12fc4f0d127ef814bd0c0ac2e
Source0:        https://github.com/zclconf/go-cty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apparentlymart/go-textseg/v15)
BuildRequires:  go(github.com/apparentlymart/go-textseg/v17)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/vmihailenco/msgpack/v5)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/zclconf/go-cty) = %{version}

Requires:       go(github.com/apparentlymart/go-textseg/v15)
Requires:       go(github.com/apparentlymart/go-textseg/v17)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/vmihailenco/msgpack/v5)
Requires:       go(golang.org/x/text)

%description
cty (pronounced "see-tie", emoji: 👀 👔, IPA: /si'tʰaɪ/) is a dynamic
type system for applications written in Go that need to represent user
supplied values without losing type information. The primary intended
use is for implementing configuration languages, but other uses may be
possible too.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
