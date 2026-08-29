# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lodepng
%global full_version 3.12.2
%global pkgname lodepng-3

Name:           rust-lodepng-3
Version:        3.12.2
Release:        %autorelease
Summary:        Rust crate "lodepng"
License:        Zlib
URL:            https://lib.rs/crates/lodepng
#!RemoteAsset:  sha256:fe7982db11054edc023a1b424dddcc65be18f71fa46ec6bde2efcfc1fb6b22da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crc32fast-1/default) >= 1.3.2
Requires:       crate(flate2-1) >= 1.1.2
Requires:       crate(rgb-0.8/bytemuck) >= 0.8.50

Provides:       crate(%{pkgname}) = %{version}

%description
Pure Rust port of LodePNG.
Source code for takopackized Rust crate "lodepng"

%package     -n %{name}+deprecated-c-ffi-default-
Summary:        Reading and writing PNG files without system dependencies - feature "_deprecated_c_ffi_default_" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.126
Provides:       crate(%{pkgname}/c-ffi) = %{version}
Provides:       crate(%{pkgname}/deprecated-c-ffi-default-) = %{version}

%description -n %{name}+deprecated-c-ffi-default-
Pure Rust port of LodePNG.
This metapackage enables feature "_deprecated_c_ffi_default_" for the Rust lodepng crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "c_ffi" feature.

%package     -n %{name}+cfzlib
Summary:        Reading and writing PNG files without system dependencies - feature "cfzlib" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/zlib-rs) >= 1.1.2
Provides:       crate(%{pkgname}/cfzlib) = %{version}
Provides:       crate(%{pkgname}/zlibrs) = %{version}

%description -n %{name}+cfzlib
Pure Rust port of LodePNG.
This metapackage enables feature "cfzlib" for the Rust lodepng crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlibrs" feature.

%package     -n %{name}+default
Summary:        Reading and writing PNG files without system dependencies - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deprecated-c-ffi-default-) = %{version}
Requires:       crate(%{pkgname}/zlibrs) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Pure Rust port of LodePNG.
This metapackage enables feature "default" for the Rust lodepng crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ngzlib
Summary:        Reading and writing PNG files without system dependencies - feature "ngzlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/zlib-ng-compat) >= 1.1.2
Provides:       crate(%{pkgname}/ngzlib) = %{version}

%description -n %{name}+ngzlib
Pure Rust port of LodePNG.
This metapackage enables feature "ngzlib" for the Rust lodepng crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-backend
Summary:        Reading and writing PNG files without system dependencies - feature "rust_backend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/rust-backend) >= 1.1.2
Provides:       crate(%{pkgname}/rust-backend) = %{version}

%description -n %{name}+rust-backend
Pure Rust port of LodePNG.
This metapackage enables feature "rust_backend" for the Rust lodepng crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
