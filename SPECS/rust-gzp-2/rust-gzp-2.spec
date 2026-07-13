# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gzp
%global full_version 2.0.2
%global pkgname gzp-2

Name:           rust-gzp-2
Version:        2.0.2
Release:        %autorelease
Summary:        Rust crate "gzp"
License:        Unlicense OR MIT
URL:            https://github.com/sstadick/gzp
#!RemoteAsset:  sha256:7abe9930717197e0ea50d8c8a1106a38b5bee0536ed4cbf4b93ba1a953f97d04
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Drop features that depend on unpackaged crates.
Patch2000:      2000-drop-unpackaged-features.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.5.0
Requires:       crate(bytes-1/default) >= 1.10.1
Requires:       crate(core-affinity-0.8/default) >= 0.8.3
Requires:       crate(flume-0.11/default) >= 0.11.1
Requires:       crate(log-0.4/default) >= 0.4.28
Requires:       crate(num-cpus-1/default) >= 1.17.0
Requires:       crate(thiserror-2/default) >= 2.0.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/deflate) = %{version}
Provides:       crate(%{pkgname}/snappy) = %{version}

%description
Source code for takopackized Rust crate "gzp"

%package     -n %{name}+any-zlib
Summary:        Parallel Compression - feature "any_zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/any-zlib) >= 1.1.4
Provides:       crate(%{pkgname}/any-zlib) = %{version}

%description -n %{name}+any-zlib
This metapackage enables feature "any_zlib" for the Rust gzp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-rust
Summary:        Parallel Compression - feature "deflate_rust"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(flate2-1/rust-backend) >= 1.1.4
Provides:       crate(%{pkgname}/deflate-rust) = %{version}

%description -n %{name}+deflate-rust
This metapackage enables feature "deflate_rust" for the Rust gzp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate-zlib
Summary:        Parallel Compression - feature "deflate_zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/any-zlib) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/libz-sys) = %{version}
Requires:       crate(flate2-1/zlib) >= 1.1.4
Requires:       crate(libz-sys-1/libc) >= 1.1.22
Provides:       crate(%{pkgname}/deflate-zlib) = %{version}

%description -n %{name}+deflate-zlib
This metapackage enables feature "deflate_zlib" for the Rust gzp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Parallel Compression - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1) >= 1.1.4
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust gzp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libz-sys
Summary:        Parallel Compression - feature "libz-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-sys-1) >= 1.1.22
Provides:       crate(%{pkgname}/libz-sys) = %{version}

%description -n %{name}+libz-sys
This metapackage enables feature "libz-sys" for the Rust gzp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
