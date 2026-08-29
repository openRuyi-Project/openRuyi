# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lzma-sys
%global full_version 0.1.20
%global pkgname lzma-sys-0.1

Name:           rust-lzma-sys-0.1
Version:        0.1.20
Release:        %autorelease
Summary:        Rust crate "lzma-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/xz2-rs
#!RemoteAsset:  sha256:5fda04ab3764e6cde78b9974eec4f779acaba7c4e84b36eca3cf77c581b85d27
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.34
Requires:       crate(libc-0.2/default) >= 0.2.51
Requires:       crate(pkg-config-0.3) >= 0.3.14
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}

%description
High level Rust bindings are available in the `xz2` crate.
Source code for takopackized Rust crate "lzma-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
