# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dns-lookup
%global full_version 4.0.2
%global pkgname dns-lookup-4

Name:           rust-dns-lookup-4
Version:        4.0.2
Release:        %autorelease
Summary:        Rust crate "dns-lookup"
License:        MIT OR Apache-2.0
URL:            https://github.com/keeperofdakeys/dns-lookup/
#!RemoteAsset:  sha256:263c0ccfc6b3b6a93e959edad4f985779e76c0b36dbb2e13e3d27c690974adf1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Patch2000:      2000-select-system-socket-dependencies.patch
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(socket2-0.6/default) >= 0.6.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dns-lookup"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
