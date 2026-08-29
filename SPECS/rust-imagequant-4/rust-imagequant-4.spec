# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imagequant
%global full_version 4.4.1
%global pkgname imagequant-4

Name:           rust-imagequant-4
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "imagequant"
License:        GPL-3.0-or-later
URL:            https://pngquant.org/lib
#!RemoteAsset:  sha256:caf5d73b959dfbe5d6b5cd3ca8de5265c7bc58297f20560a60a1d2ba6a19991f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7/default) >= 0.7.4
Requires:       crate(once-cell-1/default) >= 1.19.0
Requires:       crate(rgb-0.8/bytemuck) >= 0.8.47

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/internal-c-ffi) = %{version}
Provides:       crate(%{pkgname}/large-palettes) = %{version}

%description
For lossy PNG compression and high-quality GIF images Dual-licensed like pngquant. See https://pngquant.org for details.
Source code for takopackized Rust crate "imagequant"

%package     -n %{name}+threads
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel - feature "threads" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Requires:       crate(thread-local-1/default) >= 1.1.8
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/threads) = %{version}

%description -n %{name}+threads
For lossy PNG compression and high-quality GIF images Dual-licensed like pngquant. See https://pngquant.org for details.
This metapackage enables feature "threads" for the Rust imagequant crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
