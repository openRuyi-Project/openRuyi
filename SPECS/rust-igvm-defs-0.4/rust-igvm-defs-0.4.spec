# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name igvm_defs
%global full_version 0.4.0
%global pkgname igvm-defs-0.4

Name:           rust-igvm-defs-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "igvm_defs"
License:        MIT
URL:            https://github.com/microsoft/igvm
#!RemoteAsset:  sha256:eedd8c64460676101062f9f2ecdeb52d8f43e622da6a6c5bf5158f4ef08b0906
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitfield-struct-0.10/default) >= 0.10.0
Requires:       crate(open-enum-0.5/default) >= 0.5.2
Requires:       crate(static-assertions-1/default) >= 1.1.0
Requires:       crate(zerocopy-0.8/default) >= 0.8.14
Requires:       crate(zerocopy-0.8/derive) >= 0.8.14
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "igvm_defs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
