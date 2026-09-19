# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name completest-pty
%global full_version 1.1.0
%global pkgname completest-pty-1

Name:           rust-completest-pty-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "completest-pty"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/completest
#!RemoteAsset:  sha256:639504390a22f3fa372b16088d0569448274ef04379ff798437aab3cf811093e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(completest-1/default) >= 1.0.0
Requires:       crate(ptyprocess-0.5/default) >= 0.5.0
Requires:       crate(vt100-0.16/default) >= 0.16.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "completest-pty"

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
