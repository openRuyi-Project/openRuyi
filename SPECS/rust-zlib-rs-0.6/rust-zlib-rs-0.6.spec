# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zlib-rs
%global full_version 0.6.3
%global pkgname zlib-rs-0.6

Name:           rust-zlib-rs-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "zlib-rs"
License:        Zlib
URL:            https://github.com/trifectatechfoundation/zlib-rs
#!RemoteAsset:  sha256:3be3d40e40a133f9c916ee3f9f4fa2d9d63435b5fbe1bfc6d9dae0aa0ada1513
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/avx512) = %{version}
Provides:       crate(%{pkgname}/c-allocator) = %{version}
Provides:       crate(%{pkgname}/internal-api) = %{version}
Provides:       crate(%{pkgname}/internal-fuzz-disable-checksum) = %{version}
Provides:       crate(%{pkgname}/rust-allocator) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/vpclmulqdq) = %{version}
Provides:       crate(%{pkgname}/zlib-debug) = %{version}

%description
Source code for takopackized Rust crate "zlib-rs"

%package     -n %{name}+arbitrary
Summary:        Memory-safe zlib implementation written in rust - feature "arbitrary" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Requires:       crate(arbitrary-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}
Provides:       crate(%{pkgname}/internal-fuzz) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust zlib-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__internal-fuzz" feature.

%package     -n %{name}+default
Summary:        Memory-safe zlib implementation written in rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/c-allocator) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zlib-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Memory-safe zlib implementation written in rust - feature "quickcheck" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1) >= 1.0.3
Provides:       crate(%{pkgname}/internal-test) = %{version}
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust zlib-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__internal-test" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
