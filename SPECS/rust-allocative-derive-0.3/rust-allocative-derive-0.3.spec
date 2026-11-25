# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name allocative_derive
%global full_version 0.3.6
%global pkgname allocative-derive-0.3

Name:           rust-allocative-derive-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "allocative_derive"
License:        Apache-2.0
URL:            https://github.com/facebookexperimental/allocative
#!RemoteAsset:  sha256:614043c56c1173b800acb007b81fd0cbc0a0d7d717b71ba705fc2230d0760a23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "allocative_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
