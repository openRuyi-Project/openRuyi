# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminal-trx
%global full_version 0.2.6
%global pkgname terminal-trx-0.2

Name:           rust-terminal-trx-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "terminal-trx"
License:        MIT OR Apache-2.0
URL:            https://github.com/tautropfli/terminal-trx
#!RemoteAsset:  sha256:3b3f27d9a8a177e57545481faec87acb45c6e854ed1e5a3658ad186c106f38ed
Source:         https://static.crates.io/crates/terminal-trx/0.2.6/download#/rust-terminal-trx-0.2-0.2.6.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.152
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "terminal-trx"

%package     -n %{name}+default
Summary:        Provides a handle to the terminal of the current process - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust terminal-trx crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
