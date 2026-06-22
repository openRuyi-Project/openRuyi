# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libdisplay-info
%global full_version 0.3.0
%global pkgname libdisplay-info-0.3

Name:           rust-libdisplay-info-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "libdisplay-info"
License:        MIT
URL:            https://github.com/Smithay/libdisplay-info-rs
#!RemoteAsset:  sha256:59fd96dbb2381ff31f314f07accbdf8550febdcc5cd8761ecaf7c1763361c359
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.6.0
Requires:       crate(libc-0.2/default) >= 0.2.155
Requires:       crate(libdisplay-info-derive-0.1/default) >= 0.1.1
Requires:       crate(libdisplay-info-sys-0.3/auto) >= 0.3.0
Requires:       crate(libdisplay-info-sys-0.3/default) >= 0.3.0
Requires:       crate(thiserror-2/default) >= 2.0.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libdisplay-info"

%package     -n %{name}+v0-2
Summary:        EDID and DisplayID library - feature "v0_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libdisplay-info-sys-0.3/auto) >= 0.3.0
Requires:       crate(libdisplay-info-sys-0.3/v0-2) >= 0.3.0
Provides:       crate(%{pkgname}/v0-2) = %{version}

%description -n %{name}+v0-2
This metapackage enables feature "v0_2" for the Rust libdisplay-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v0-3
Summary:        EDID and DisplayID library - feature "v0_3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libdisplay-info-sys-0.3/auto) >= 0.3.0
Requires:       crate(libdisplay-info-sys-0.3/v0-3) >= 0.3.0
Provides:       crate(%{pkgname}/v0-3) = %{version}

%description -n %{name}+v0-3
This metapackage enables feature "v0_3" for the Rust libdisplay-info crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
