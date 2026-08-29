# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serial_test_derive
%global full_version 3.5.0
%global pkgname serial-test-derive-3

Name:           rust-serial-test-derive-3
Version:        3.5.0
Release:        %autorelease
Summary:        Rust crate "serial_test_derive"
License:        MIT
URL:            https://github.com/palfrey/serial_test/
#!RemoteAsset:  sha256:94e153fc76e1c6a068703d6d29c508a0b15c061c4b7e43da59cc097bc342673c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.60
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/file-locks) = %{version}
Provides:       crate(%{pkgname}/test-logging) = %{version}

%description
Source code for takopackized Rust crate "serial_test_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
