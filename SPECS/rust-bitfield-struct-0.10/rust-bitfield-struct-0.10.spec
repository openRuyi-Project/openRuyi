# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitfield-struct
%global full_version 0.10.1
%global pkgname bitfield-struct-0.10

Name:           rust-bitfield-struct-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "bitfield-struct"
License:        MIT
URL:            https://github.com/wrenger/bitfield-struct-rs.git
#!RemoteAsset:  sha256:2be5a46ba01b60005ae2c51a36a29cfe134bcacae2dd5cedcd4615fbaad1494b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bitfield-struct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
