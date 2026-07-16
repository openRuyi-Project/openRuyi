# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ahash
%global full_version 0.7.8
%global pkgname ahash-0.7

Name:           rust-ahash-0.7
Version:        0.7.8
Release:        %autorelease
Summary:        Rust crate "ahash"
License:        MIT OR Apache-2.0
URL:            https://github.com/tkaitchuck/ahash
#!RemoteAsset:  sha256:891477e0c6a8957309ee5c45a6368af3ae14bb510732d2684ffa19af310920f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.2/default) >= 0.2.3
Requires:       crate(once-cell-1/alloc) >= 1.13.1
Requires:       crate(version-check-0.9) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ahash"

%package     -n %{name}+atomic-polyfill
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "atomic-polyfill"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atomic-polyfill-1/default) >= 1.0.1
Requires:       crate(once-cell-1/alloc) >= 1.13.1
Requires:       crate(once-cell-1/atomic-polyfill) >= 1.13.1
Provides:       crate(%{pkgname}/atomic-polyfill) = %{version}

%description -n %{name}+atomic-polyfill
This metapackage enables feature "atomic-polyfill" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-random
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "const-random" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-random-0.1/default) >= 0.1.12
Provides:       crate(%{pkgname}/compile-time-rng) = %{version}
Provides:       crate(%{pkgname}/const-random) = %{version}

%description -n %{name}+const-random
This metapackage enables feature "const-random" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compile-time-rng" feature.

%package     -n %{name}+serde
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.117
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
