# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name page_size
%global full_version 0.6.0
%global pkgname page-size-0.6

Name:           rust-page-size-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "page_size"
License:        MIT OR Apache-2.0
URL:            https://github.com/Elzair/page_size_rs
#!RemoteAsset:  sha256:30d5b2194ed13191c1999ae0704b7839fb18384fa22e49b57eeaa97d79ce40da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Provides an easy, fast, cross-platform way to retrieve the memory page size.
Source code for takopackized Rust crate "page_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
