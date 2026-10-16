# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curve25519-dalek
%global full_version 4.1.3
%global pkgname curve25519-dalek-4

Name:           rust-curve25519-dalek-4
Version:        4.1.3
Release:        %autorelease
Summary:        Rust crate "curve25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:97fb8b7c4503de7d6ae7b42ab72a5a59857b4c937ec27a3d4539dba95b5ab2be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.2/default) >= 0.2.6
Requires:       crate(curve25519-dalek-derive-0.1/default) >= 0.1.0
Requires:       crate(fiat-crypto-0.2) >= 0.2.1
Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(subtle-2) >= 2.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/legacy-compatibility) = %{version}
Provides:       crate(%{pkgname}/precomputed-tables) = %{version}

%description
Source code for takopackized Rust crate "curve25519-dalek"

%package     -n %{name}+alloc
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/precomputed-tables) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "ff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ff-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/ff) = %{version}

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "group"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(group-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/group) = %{version}

%description -n %{name}+group
This metapackage enables feature "group" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group-bits
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "group-bits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/group) = %{version}
Requires:       crate(ff-0.13/bits) >= 0.13.0
Provides:       crate(%{pkgname}/group-bits) = %{version}

%description -n %{name}+group-bits
This metapackage enables feature "group-bits" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6) >= 0.6.4
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
