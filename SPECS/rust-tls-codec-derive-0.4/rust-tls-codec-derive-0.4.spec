# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tls_codec_derive
%global full_version 0.4.2
%global pkgname tls-codec-derive-0.4

Name:           rust-tls-codec-derive-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "tls_codec_derive"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/tls_codec/derive
#!RemoteAsset:  sha256:2d2e76690929402faae40aebdda620a2c0e25dd6d3b9afe48867dfd95991f4bd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "tls_codec_derive"

%package     -n %{name}+conditional-deserialization
Summary:        Derive macros for the tls_codec trait - feature "conditional_deserialization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Provides:       crate(%{pkgname}/conditional-deserialization) = %{version}

%description -n %{name}+conditional-deserialization
This metapackage enables feature "conditional_deserialization" for the Rust tls_codec_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
