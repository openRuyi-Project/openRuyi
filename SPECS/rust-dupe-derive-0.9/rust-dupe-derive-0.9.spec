# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dupe_derive
%global full_version 0.9.1
%global pkgname dupe-derive-0.9

Name:           rust-dupe-derive-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "dupe_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebookincubator/gazebo
#!RemoteAsset:  sha256:83e195b4945e88836d826124af44fdcb262ec01ef94d44f14f4fb5103f19892a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.3
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dupe_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
