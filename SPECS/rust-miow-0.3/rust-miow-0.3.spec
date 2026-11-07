# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miow
%global full_version 0.3.7
%global pkgname miow-0.3

Name:           rust-miow-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "miow"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/miow
#!RemoteAsset:  sha256:b9f1c5b025cda876f66ef43a113f91ebc9f4ccef34843000e0adf6ebbab84e21
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/default) >= 0.3.3
Requires:       crate(winapi-0.3/fileapi) >= 0.3.3
Requires:       crate(winapi-0.3/handleapi) >= 0.3.3
Requires:       crate(winapi-0.3/ioapiset) >= 0.3.3
Requires:       crate(winapi-0.3/minwindef) >= 0.3.3
Requires:       crate(winapi-0.3/namedpipeapi) >= 0.3.3
Requires:       crate(winapi-0.3/ntdef) >= 0.3.3
Requires:       crate(winapi-0.3/std) >= 0.3.3
Requires:       crate(winapi-0.3/synchapi) >= 0.3.3
Requires:       crate(winapi-0.3/winerror) >= 0.3.3
Requires:       crate(winapi-0.3/winsock2) >= 0.3.3
Requires:       crate(winapi-0.3/ws2def) >= 0.3.3
Requires:       crate(winapi-0.3/ws2ipdef) >= 0.3.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "miow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
