# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name brotli-decompressor
%global full_version 4.0.3
%global pkgname brotli-decompressor-4

Name:           rust-brotli-decompressor-4
Version:        4.0.3
Release:        %autorelease
Summary:        Rust crate "brotli-decompressor"
License:        BSD-3-Clause OR MIT
URL:            https://github.com/dropbox/rust-brotli-decompressor
#!RemoteAsset:  sha256:a334ef7c9e23abf0ce748e8cd309037da93e606ad52eb372e4ce327a0dcfbdfd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(alloc-no-stdlib-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/benchmark) = %{version}
Provides:       crate(%{pkgname}/disable-timer) = %{version}
Provides:       crate(%{pkgname}/ffi-api) = %{version}
Provides:       crate(%{pkgname}/pass-through-ffi-panics) = %{version}
Provides:       crate(%{pkgname}/seccomp) = %{version}

%description
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. Alternatively, --features=unsafe turns off array bounds checks and memory initialization but provides a safe interface for the caller.  Without adding the --features=unsafe argument, all included code is safe. For compression in addition to this library, download https://github.com/dropbox/rust-brotli
Source code for takopackized Rust crate "brotli-decompressor"

%package     -n %{name}+alloc-stdlib
Summary:        Brotli decompressor that with an interface avoiding the rust stdlib - feature "alloc-stdlib" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(alloc-stdlib-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/alloc-stdlib) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc-stdlib
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. Alternatively, --features=unsafe turns off array bounds checks and memory initialization but provides a safe interface for the caller.  Without adding the --features=unsafe argument, all included code is safe. For compression in addition to this library, download https://github.com/dropbox/rust-brotli
This metapackage enables feature "alloc-stdlib" for the Rust brotli-decompressor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%package     -n %{name}+unsafe
Summary:        Brotli decompressor that with an interface avoiding the rust stdlib - feature "unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(alloc-no-stdlib-2/unsafe) >= 2.0.0
Requires:       crate(alloc-stdlib-0.2/unsafe) >= 0.2.0
Provides:       crate(%{pkgname}/unsafe) = %{version}

%description -n %{name}+unsafe
This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. Alternatively, --features=unsafe turns off array bounds checks and memory initialization but provides a safe interface for the caller.  Without adding the --features=unsafe argument, all included code is safe. For compression in addition to this library, download https://github.com/dropbox/rust-brotli
This metapackage enables feature "unsafe" for the Rust brotli-decompressor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
