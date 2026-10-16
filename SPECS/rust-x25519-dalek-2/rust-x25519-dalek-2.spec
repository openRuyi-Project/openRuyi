# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x25519-dalek
%global full_version 2.0.1
%global pkgname x25519-dalek-2

Name:           rust-x25519-dalek-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "x25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:c7e468321c81fb07fa7f4c636c3972b9100f0346e5b6a9f2bd0603a52f7ed277
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curve25519-dalek-4) >= 4.0.0
Requires:       crate(rand-core-0.6) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/reusable-secrets) = %{version}
Provides:       crate(%{pkgname}/static-secrets) = %{version}

%description
Source code for takopackized Rust crate "x25519-dalek"

%package     -n %{name}+alloc
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/alloc) >= 4.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(zeroize-1/alloc) >= 1.0.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/precomputed-tables) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+precomputed-tables
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "precomputed-tables"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/precomputed-tables) >= 4.0.0
Provides:       crate(%{pkgname}/precomputed-tables) = %{version}

%description -n %{name}+precomputed-tables
This metapackage enables feature "precomputed-tables" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/serde) >= 4.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using curve25519-dalek - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/zeroize) >= 4.0.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust x25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
