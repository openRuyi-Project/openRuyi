# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qudp
%global full_version 0.8.1
%global pkgname qudp-0.8

Name:           rust-qudp-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "qudp"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:97f814f5448612fe66c307b3da58284c3ee8839138ae395e72d6dd1bd65e7cc2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(nix-0.31/default) >= 0.31.0
Requires:       crate(nix-0.31/net) >= 0.31.0
Requires:       crate(nix-0.31/socket) >= 0.31.0
Requires:       crate(nix-0.31/uio) >= 0.31.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(socket2-0.6/all) >= 0.6.0
Requires:       crate(socket2-0.6/default) >= 0.6.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gso) = %{version}

%description
Source code for takopackized Rust crate "qudp"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
