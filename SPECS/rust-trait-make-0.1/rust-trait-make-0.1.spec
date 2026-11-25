# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name trait-make
%global full_version 0.1.0
%global pkgname trait-make-0.1

Name:           rust-trait-make-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "trait-make"
License:        MIT OR Apache-2.0
URL:            https://github.com/Sherlock-Holo/impl-trait-utils
#!RemoteAsset:  sha256:96cbd06a7b648f1603e60d75d9ed295d096b340d30e9f9324f4b512b5d40cd92
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "trait-make"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
