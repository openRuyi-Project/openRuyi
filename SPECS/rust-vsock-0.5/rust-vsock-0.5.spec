# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vsock
%global full_version 0.5.4
%global pkgname vsock-0.5

Name:           rust-vsock-0.5
Version:        0.5.4
Release:        %autorelease
Summary:        Rust crate "vsock"
License:        Apache-2.0
URL:            https://github.com/rust-vsock/vsock-rs
#!RemoteAsset:  sha256:6ba782755fc073877e567c2253c0be48e4aa9a254c232d36d3985dfae0bd5205
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.182
Requires:       crate(nix-0.31/default) >= 0.31.2
Requires:       crate(nix-0.31/ioctl) >= 0.31.2
Requires:       crate(nix-0.31/socket) >= 0.31.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vsock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
