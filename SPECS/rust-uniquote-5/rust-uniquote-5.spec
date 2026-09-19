# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uniquote
%global full_version 5.0.0
%global pkgname uniquote-5

Name:           rust-uniquote-5
Version:        5.0.0
Release:        %autorelease
Summary:        Rust crate "uniquote"
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://github.com/dylni/uniquote
#!RemoteAsset:  sha256:b56132e1afba089ff971694f5fa858b1b715b58156bd1f1503d6d0a6c3c779f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "uniquote"

%package     -n %{name}+os-str-bytes
Summary:        Quote strings for clear display in output - feature "os_str_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(os-str-bytes-7/raw-os-str) >= 7.2.0
Provides:       crate(%{pkgname}/os-str-bytes) = %{version}

%description -n %{name}+os-str-bytes
This metapackage enables feature "os_str_bytes" for the Rust uniquote crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE-THIRD-PARTY
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
