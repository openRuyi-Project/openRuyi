# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-internal-macros
%global full_version 0.2.9
%global pkgname stdweb-internal-macros-0.2

Name:           rust-stdweb-internal-macros-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "stdweb-internal-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:58fa5ff6ad0d98d1ffa8cb115892b6e69d67799f6763e162a1c9db421dc22e11
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base-x-0.2/default) >= 0.2.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(sha1-0.6/default) >= 0.6.0
Requires:       crate(syn-1/clone-impls) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0
Requires:       crate(syn-1/parsing) >= 1.0.0
Requires:       crate(syn-1/printing) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-internal-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
