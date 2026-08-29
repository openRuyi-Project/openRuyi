# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen-rust-macro
%global full_version 0.51.0
%global pkgname wit-bindgen-rust-macro-0.51

Name:           rust-wit-bindgen-rust-macro-0.51
Version:        0.51.0
Release:        %autorelease
Summary:        Rust crate "wit-bindgen-rust-macro"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:0c0f9bfd77e6a48eccf51359e3ae77140a7f50b1e2ebfe62422d8afdaffab17a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.72
Requires:       crate(prettyplease-0.2/default) >= 0.2.20
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.89
Requires:       crate(syn-2/printing) >= 2.0.89
Requires:       crate(wit-bindgen-core-0.51/default) >= 0.51.0
Requires:       crate(wit-bindgen-rust-0.51/default) >= 0.51.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wit-bindgen-rust-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
