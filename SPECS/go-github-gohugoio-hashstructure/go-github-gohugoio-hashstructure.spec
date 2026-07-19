# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hashstructure
%define go_import_path  github.com/gohugoio/hashstructure

Name:           go-github-gohugoio-hashstructure
Version:        0.6.0
Release:        %autorelease
Summary:        Get hash values for arbitrary values in Go (golang)
License:        MIT
URL:            https://github.com/gohugoio/hashstructure
#!RemoteAsset:  sha256:7e8d9f4d475b7817316a110cb2deb5585d99f7a7c55949adfd4eeea81915cc91
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)

Provides:       go(github.com/gohugoio/hashstructure) = %{version}

%description
hashstructure is a Go library for creating a unique hash value for
arbitrary values in Go.

This can be used to key values in a hash (for use in a map, set, etc.)
that are complex. The most common use case is comparing two values
without sending data across the network, caching values locally (de-dup),
and so on.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
