# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libspa-sys
%global full_version 0.9.2
%global pkgname libspa-sys-0.9

Name:           rust-libspa-sys-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "libspa-sys"
License:        MIT
URL:            https://pipewire.org
#!RemoteAsset:  sha256:901049455d2eb6decf9058235d745237952f4804bc584c5fcb41412e6adcc6e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.72) >= 0.72.0
Requires:       crate(bindgen-0.72/experimental) >= 0.72.0
Requires:       crate(bindgen-0.72/runtime) >= 0.72.0
Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(system-deps-7) >= 7.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v0-3-65) = %{version}

%description
Source code for takopackized Rust crate "libspa-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
