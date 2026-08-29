# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nanorand
%global full_version 0.7.0
%global pkgname nanorand-0.7

Name:           rust-nanorand-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "nanorand"
License:        Zlib
URL:            https://github.com/Absolucy/nanorand-rs
#!RemoteAsset:  sha256:6a51313c5820b0b02bd422f4b44776fbf47961755c74ce64afc73bfad10226c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/chacha) = %{version}
Provides:       crate(%{pkgname}/pcg64) = %{version}
Provides:       crate(%{pkgname}/rdseed) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/wyrand) = %{version}

%description
Source code for takopackized Rust crate "nanorand"

%package     -n %{name}+default
Summary:        Tiny, fast, zero-dep library for random number generation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chacha) = %{version}
Requires:       crate(%{pkgname}/pcg64) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tls) = %{version}
Requires:       crate(%{pkgname}/wyrand) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust nanorand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Tiny, fast, zero-dep library for random number generation - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.2/default) >= 0.2.5
Requires:       crate(getrandom-0.2/js) >= 0.2.5
Requires:       crate(getrandom-0.2/rdrand) >= 0.2.5
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust nanorand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls
Summary:        Tiny, fast, zero-dep library for random number generation - feature "tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wyrand) = %{version}
Provides:       crate(%{pkgname}/tls) = %{version}

%description -n %{name}+tls
This metapackage enables feature "tls" for the Rust nanorand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Tiny, fast, zero-dep library for random number generation - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.5.3
Requires:       crate(zeroize-1/zeroize-derive) >= 1.5.3
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust nanorand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
