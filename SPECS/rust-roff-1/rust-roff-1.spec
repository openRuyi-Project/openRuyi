# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name roff
%global full_version 1.1.1
%global pkgname roff-1

Name:           rust-roff-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "roff"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/roff-rs
#!RemoteAsset:  sha256:323c417e1d9665a65b263ec744ba09030cfb277e9daa0b018a4ab62e57bc8189
Source:         https://static.crates.io/crates/roff/1.1.1/download#/rust-roff-1-1.1.1.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "roff"

%package     -n %{name}+default
Summary:        ROFF (man page format) generation library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust roff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
