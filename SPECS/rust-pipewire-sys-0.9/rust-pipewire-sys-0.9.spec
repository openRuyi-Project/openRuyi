# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pipewire-sys
%global full_version 0.9.2
%global pkgname pipewire-sys-0.9

Name:           rust-pipewire-sys-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "pipewire-sys"
License:        MIT
URL:            https://pipewire.org
#!RemoteAsset:  sha256:cb028afee0d6ca17020b090e3b8fa2d7de23305aef975c7e5192a5050246ea36
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.72) >= 0.72.0
Requires:       crate(bindgen-0.72/runtime) >= 0.72.0
Requires:       crate(libspa-sys-0.9/default) >= 0.9.0
Requires:       crate(system-deps-7) >= 7.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pipewire-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
