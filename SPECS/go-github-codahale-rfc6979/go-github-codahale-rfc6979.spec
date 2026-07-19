# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rfc6979
%define go_import_path  github.com/codahale/rfc6979
%define commit_id 6a90f24967ebb1aa57b22f74a13dbb3faad8cf3d

Name:           go-github-codahale-rfc6979
Version:        0+git20260719.6a90f24
Release:        %autorelease
Summary:        Go implementation of RFC 6979's deterministic DSA
License:        MIT
URL:            https://github.com/codahale/rfc6979
#!RemoteAsset:  sha256:cf44378356998f65ad363a17307ac5eb52ebd0e7ddc18fa02c7576c59461e295
Source0:        https://github.com/codahale/rfc6979/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/codahale/rfc6979) = %{version}

%description
A Go implementation of RFC 6979 (https://tools.ietf.org/html/rfc6979)'s
deterministic DSA/ECDSA signature scheme.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
