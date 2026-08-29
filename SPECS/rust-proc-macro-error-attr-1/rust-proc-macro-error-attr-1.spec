# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error-attr
%global full_version 1.0.4
%global pkgname proc-macro-error-attr-1

Name:           rust-proc-macro-error-attr-1
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "proc-macro-error-attr"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/CreepySkeleton/proc-macro-error
#!RemoteAsset:  sha256:a1be40180e52ecc98ad80b184934baf3d0d29f979574e439af5a55274b35f869
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(version-check-0.9) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-error-attr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
