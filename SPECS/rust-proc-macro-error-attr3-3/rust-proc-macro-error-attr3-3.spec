# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error-attr3
%global full_version 3.0.2
%global pkgname proc-macro-error-attr3-3

Name:           rust-proc-macro-error-attr3-3
Version:        3.0.2
Release:        %autorelease
Summary:        Rust crate "proc-macro-error-attr3"
License:        MIT OR Apache-2.0
URL:            https://github.com/gamma0987/proc-macro-error3
#!RemoteAsset:  sha256:34e4dd828515431dd6c4a030d26f7eaed7dd4778226e9d2bb968d65ca4ec3d4d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-error-attr3"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
