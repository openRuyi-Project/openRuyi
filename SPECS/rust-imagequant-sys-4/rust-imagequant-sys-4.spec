# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imagequant-sys
%global full_version 4.1.0
%global pkgname imagequant-sys-4

Name:           rust-imagequant-sys-4
Version:        4.1.0
Release:        %autorelease
Summary:        Rust crate "imagequant-sys"
License:        GPL-3.0-or-later
URL:            https://pngquant.org/lib
#!RemoteAsset:  sha256:b5361d7aab1d0c5623172cd6d18920bf21ef56f6e21d7290f1e31e0794c4a76e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.5.0
Requires:       crate(imagequant-4/internal-c-ffi) >= 4.4.0
Requires:       crate(libc-0.2/default) >= 0.2.153

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/capi) = %{version}

%description
C API/FFI libimagequant that powers pngquant lossy PNG compressor.
Dual-licensed like pngquant. See https://pngquant.org for details.
Source code for takopackized Rust crate "imagequant-sys"

%package     -n %{name}+default
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(imagequant-4/default) >= 4.4.0
Requires:       crate(imagequant-4/internal-c-ffi) >= 4.4.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
C API/FFI libimagequant that powers pngquant lossy PNG compressor.
Dual-licensed like pngquant. See https://pngquant.org for details.
This metapackage enables feature "default" for the Rust imagequant-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+threads
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel - feature "threads"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(imagequant-4/internal-c-ffi) >= 4.4.0
Requires:       crate(imagequant-4/threads) >= 4.4.0
Provides:       crate(%{pkgname}/threads) = %{version}

%description -n %{name}+threads
C API/FFI libimagequant that powers pngquant lossy PNG compressor.
Dual-licensed like pngquant. See https://pngquant.org for details.
This metapackage enables feature "threads" for the Rust imagequant-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%license COPYRIGHT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
