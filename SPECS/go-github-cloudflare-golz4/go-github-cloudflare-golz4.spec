# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golz4
%define go_import_path  github.com/cloudflare/golz4
%define commit_id       ef862a3cdc58a6f1fee4e3af3d44fbe279194cde

Name:           go-github-cloudflare-golz4
Version:        0+git20260922.ef862a3
Release:        %autorelease
Summary:        Go bindings for LZ4 compression
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/cloudflare/golz4
#!RemoteAsset:  sha256:8102d1eed874ed212f463b14e38ee865a3fe85c4a8f97587d77db2121522e4ff
Source0:        https://github.com/cloudflare/golz4/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The bundled LZ4 r126 crashes in high-compression tests with the current toolchain.
Patch2000:      2000-Use-system-LZ4.patch

# Exact compressed byte counts vary with the system LZ4 version.
BuildOption(check):  -skip '^TestCompressionHCLevels$'

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(liblz4)

Provides:       go(github.com/cloudflare/golz4) = %{version}

Requires:       pkgconfig(liblz4)

%description
This library provides Go bindings for LZ4 compression and
high-compression routines.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
