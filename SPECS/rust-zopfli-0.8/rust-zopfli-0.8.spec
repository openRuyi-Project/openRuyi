# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zopfli
%global full_version 0.8.3
%global pkgname zopfli-0.8

Name:           rust-zopfli-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "zopfli"
License:        Apache-2.0
URL:            https://github.com/zopfli-rs/zopfli
#!RemoteAsset:  sha256:f05cd8797d63865425ff89b5c4a48804f35ba0ce8d125800027ad6017d2b5249
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bumpalo-3/default) >= 3.19.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "zopfli"

%package     -n %{name}+default
Summary:        The Zopfli compression algorithm - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gzip) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/zlib) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zopfli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gzip
Summary:        The Zopfli compression algorithm - feature "gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1) >= 1.5.0
Provides:       crate(%{pkgname}/gzip) = %{version}

%description -n %{name}+gzip
This metapackage enables feature "gzip" for the Rust zopfli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        The Zopfli compression algorithm - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1/nightly) >= 1.5.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust zopfli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        The Zopfli compression algorithm - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1/std) >= 1.5.0
Requires:       crate(log-0.4/default) >= 0.4.28
Requires:       crate(simd-adler32-0.3/std) >= 0.3.7
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zopfli crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        The Zopfli compression algorithm - feature "zlib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simd-adler32-0.3) >= 0.3.7
Provides:       crate(%{pkgname}/zlib) = %{version}

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust zopfli crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
