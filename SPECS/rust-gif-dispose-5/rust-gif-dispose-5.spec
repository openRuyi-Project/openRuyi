# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gif-dispose
%global full_version 5.0.1
%global pkgname gif-dispose-5

Name:           rust-gif-dispose-5
Version:        5.0.1
Release:        %autorelease
Summary:        Rust crate "gif-dispose"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/gif-dispose
#!RemoteAsset:  sha256:5e1aa07391f3d9c279f388cea6faf291555dd891df59bed01d4378583df946ac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gif-0.13/std) >= 0.13.1
Requires:       crate(imgref-1/default) >= 1.10.1
Requires:       crate(rgb-0.8/bytemuck) >= 0.8.43

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
The gif crate only exposes raw frame data that is not sufficient to render GIFs properly. GIF requires special composing of frames which, as this crate shows, is non-trivial.
Source code for takopackized Rust crate "gif-dispose"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
