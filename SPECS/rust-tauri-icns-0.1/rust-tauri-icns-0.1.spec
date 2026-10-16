# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tauri-icns
%global full_version 0.1.0
%global pkgname tauri-icns-0.1

Name:           rust-tauri-icns-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "tauri-icns"
License:        MIT
URL:            https://github.com/tauri-apps/rust-icns
#!RemoteAsset:  sha256:03b7eb4d0d43724ba9ba6a6717420ee68aee377816a3edbb45db8c18862b1431
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tauri-icns"

%package     -n %{name}+png
Summary:        Encoding/decoding Apple Icon Image (.icns) files - feature "png" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(png-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/png) = %{version}
Provides:       crate(%{pkgname}/pngio) = %{version}

%description -n %{name}+png
This metapackage enables feature "png" for the Rust tauri-icns crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "pngio" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
