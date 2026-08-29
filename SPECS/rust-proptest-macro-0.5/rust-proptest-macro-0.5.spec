# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proptest-macro
%global full_version 0.5.0
%global pkgname proptest-macro-0.5

Name:           rust-proptest-macro-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "proptest-macro"
License:        MIT OR Apache-2.0
URL:            https://proptest-rs.github.io/proptest/proptest/index.html
#!RemoteAsset:  sha256:efaa288b896cb2b345da7b7f2110ab19e51565b83495b56fcec98a62f8b1f33e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(convert-case-0.11/default) >= 0.11.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.114
Requires:       crate(syn-2/full) >= 2.0.114
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proptest-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
