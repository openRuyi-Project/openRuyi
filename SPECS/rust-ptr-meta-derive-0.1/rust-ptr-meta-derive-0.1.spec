# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ptr_meta_derive
%global full_version 0.1.4
%global pkgname ptr-meta-derive-0.1

Name:           rust-ptr-meta-derive-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "ptr_meta_derive"
License:        MIT
URL:            https://github.com/djkoloski/ptr_meta
#!RemoteAsset:  sha256:16b845dbfca988fa33db069c0e230574d15a3088f147a87b64c7589eb662c9ac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ptr_meta_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
