# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs-sys-next
%global full_version 0.1.2
%global pkgname dirs-sys-next-0.1

Name:           rust-dirs-sys-next-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "dirs-sys-next"
License:        MIT OR Apache-2.0
URL:            https://github.com/xdg-rs/dirs/tree/master/dirs-sys
#!RemoteAsset:  sha256:4ebda144c4fe02d1f7ea1a7d9641b6fc6b580adcfa024ae48797ecdeb6825b4d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(redox-users-0.4) >= 0.4.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/knownfolders) >= 0.3.0
Requires:       crate(winapi-0.3/objbase) >= 0.3.0
Requires:       crate(winapi-0.3/shlobj) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs-sys-next"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
