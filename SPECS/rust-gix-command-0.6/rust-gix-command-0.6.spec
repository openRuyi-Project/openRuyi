# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-command
%global full_version 0.6.5
%global pkgname gix-command-0.6

Name:           rust-gix-command-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "gix-command"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:46f9c425730a654835351e6da8c3c69ba1804f8b8d4e96d027254151138d5c64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-path-0.10/default) >= 0.10.21
Requires:       crate(gix-quote-0.6/default) >= 0.6.1
Requires:       crate(gix-trace-0.1/default) >= 0.1.17
Requires:       crate(shell-words-1/default) >= 1.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-command"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
