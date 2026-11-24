# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name data-encoding-macro-internal
%global full_version 0.1.17
%global pkgname data-encoding-macro-internal-0.1

Name:           rust-data-encoding-macro-internal-0.1
Version:        0.1.17
Release:        %autorelease
Summary:        Rust crate "data-encoding-macro-internal"
License:        MIT
URL:            https://github.com/ia0/data-encoding
#!RemoteAsset:  sha256:7ab67060fc6b8ef687992d439ca0fa36e7ed17e9a0b16b25b601e8757df720de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(data-encoding-2/alloc) >= 2.10.0
Requires:       crate(syn-1/parsing) >= 1.0.0
Requires:       crate(syn-1/proc-macro) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "data-encoding-macro-internal"

%prep -a
# Cargo ships the original manifest as a backup.
rm -f Cargo.toml.orig

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
