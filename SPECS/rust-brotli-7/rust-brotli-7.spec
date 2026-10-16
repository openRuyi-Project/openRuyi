# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name brotli
%global full_version 7.0.0
%global pkgname brotli-7

Name:           rust-brotli-7
Version:        7.0.0
Release:        %autorelease
Summary:        Rust crate "brotli"
License:        BSD-3-Clause AND MIT
URL:            https://github.com/dropbox/rust-brotli
#!RemoteAsset:  sha256:cc97b8f16f944bba54f0433f07e30be199b6dc2bd25937444bbad560bcea29bd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(alloc-no-stdlib-2/default) >= 2.0.0
Requires:       crate(brotli-decompressor-4) >= 4.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/billing) = %{version}
Provides:       crate(%{pkgname}/disallow-large-window-size) = %{version}
Provides:       crate(%{pkgname}/external-literal-probability) = %{version}
Provides:       crate(%{pkgname}/float64) = %{version}
Provides:       crate(%{pkgname}/floating-point-context-mixing) = %{version}
Provides:       crate(%{pkgname}/no-stdlib-ffi-binding) = %{version}
Provides:       crate(%{pkgname}/pass-through-ffi-panics) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/vector-scratch-space) = %{version}

%description
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
Source code for takopackized Rust crate "brotli"

%package     -n %{name}+alloc-stdlib
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "alloc-stdlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(alloc-stdlib-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/alloc-stdlib) = %{version}

%description -n %{name}+alloc-stdlib
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "alloc-stdlib" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+benchmark
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "benchmark"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-4/benchmark) >= 4.0.0
Provides:       crate(%{pkgname}/benchmark) = %{version}

%description -n %{name}+benchmark
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "benchmark" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+disable-timer
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "disable-timer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-4/disable-timer) >= 4.0.0
Provides:       crate(%{pkgname}/disable-timer) = %{version}

%description -n %{name}+disable-timer
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "disable-timer" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi-api
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "ffi-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-4/ffi-api) >= 4.0.0
Provides:       crate(%{pkgname}/ffi-api) = %{version}

%description -n %{name}+ffi-api
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "ffi-api" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+seccomp
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "seccomp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-decompressor-4/seccomp) >= 4.0.0
Provides:       crate(%{pkgname}/seccomp) = %{version}

%description -n %{name}+seccomp
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "seccomp" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "sha2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/validation) = %{version}

%description -n %{name}+sha2
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "sha2" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "validation" feature.

%package     -n %{name}+std
Summary:        Brotli compressor and decompressor that with an interface avoiding the rust stdlib - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc-stdlib) = %{version}
Requires:       crate(brotli-decompressor-4/std) >= 4.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.
This metapackage enables feature "std" for the Rust brotli crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
