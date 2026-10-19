# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ws
%define go_import_path  github.com/gobwas/ws

Name:           go-github-gobwas-ws
Version:        1.4.0
Release:        %autorelease
Summary:        Tiny WebSocket library for Go.
License:        MIT
URL:            https://github.com/gobwas/ws
#!RemoteAsset:  sha256:a251099ad7b7791be0e96f646ec486d8c047d44107eb9219e18b74d76d6529da
Source0:        https://github.com/gobwas/ws/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Handle Go 1.27's short compressor EOF blocks without corrupting PMCE frames.
# Submitted upstream: https://github.com/gobwas/ws/pull/227
Patch2000:      2000-handle-short-compressor-eof-blocks.patch
# Follow-up simplification from the same upstream pull request.
Patch2001:      2001-simplify-flush-state.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobwas/httphead)
BuildRequires:  go(github.com/gobwas/pool)

Provides:       go(github.com/gobwas/ws) = %{version}

Requires:       go(github.com/gobwas/httphead)
Requires:       go(github.com/gobwas/pool)

%description
RFC6455 WebSocket implementation in Go.

Features

 * Zero-copy upgrade
 * No intermediate allocations during I/O
 * Low-level API which allows to build your own logic of packet handling
   and
   buffers reuse
 * High-level wrappers and helpers around API in wsutil package, which
   allow
   to start fast without digging the protocol internals

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
