# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-hack
%global full_version 0.5.19
%global pkgname proc-macro-hack-0.5

Name:           rust-proc-macro-hack-0.5
Version:        0.5.19
Release:        %autorelease
Summary:        Rust crate "proc-macro-hack"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/proc-macro-hack
#!RemoteAsset:  sha256:dbf0c48bc1d91375ae5c3cd81e3722dff1abcf81a30960240640d223f59fe0e5
Source:         https://static.crates.io/crates/proc-macro-hack/0.5.19/download#/rust-proc-macro-hack-0.5-0.5.19.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-hack"

%package     -n %{name}+default
Summary:        Procedural macros in expression position - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proc-macro-hack crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
