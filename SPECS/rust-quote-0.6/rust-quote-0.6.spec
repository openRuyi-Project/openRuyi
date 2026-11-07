# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quote
%global full_version 0.6.13
%global pkgname quote-0.6

Name:           rust-quote-0.6
Version:        0.6.13
Release:        %autorelease
Summary:        Rust crate "quote"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/quote
#!RemoteAsset:  sha256:6ce23b6b870e8f94f81fb0a363d65d86675884b34a09043c81e5562f11c1f8e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-0.4) >= 0.4.21

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "quote"

%package     -n %{name}+proc-macro
Summary:        Quasi-quoting macro quote!(...) - feature "proc-macro" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-0.4/proc-macro) >= 0.4.21
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust quote crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
