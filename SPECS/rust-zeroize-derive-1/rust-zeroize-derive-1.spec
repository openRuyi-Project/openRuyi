# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zeroize_derive
%global full_version 1.5.0
%global pkgname zeroize-derive-1

Name:           rust-zeroize-derive-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "zeroize_derive"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:3c50655cbb0fe3fc43170059e702f1ce5e19b84cec58dc87b037a09935c2f328
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/visit) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zeroize_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
