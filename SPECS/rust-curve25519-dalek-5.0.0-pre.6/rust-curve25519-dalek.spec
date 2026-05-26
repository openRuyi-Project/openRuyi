# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curve25519-dalek
%global full_version 5.0.0-pre.6
%global pkgname curve25519-dalek-5.0.0-pre.6

Name:           rust-curve25519-dalek-5.0.0-pre.6
Version:        5.0.0
Release:        %autorelease
Summary:        Rust crate "curve25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:335f1947f241137a14106b6f5acc5918a5ede29c9d71d3f2cb1678d5075d9fc3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(cpufeatures-0.2/default) >= 0.2.17
Requires:       crate(curve25519-dalek-derive-0.1/default) >= 0.1.1
Requires:       crate(fiat-crypto-0.3) >= 0.3.0
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Requires:       crate(subtle-2.0/const-generics) >= 2.6.1
Provides:       crate(curve25519-dalek) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/legacy-compatibility)
Provides:       crate(%{pkgname}/precomputed-tables)

%description
Source code for takopackized Rust crate "curve25519-dalek"

%package     -n %{name}+alloc
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/precomputed-tables)
Requires:       crate(%{pkgname}/zeroize)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/block-api) >= 0.11.3
Provides:       crate(%{pkgname}/digest)
Provides:       crate(%{pkgname}/lizard)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "lizard" feature.

%package     -n %{name}+ff
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "ff"
Requires:       crate(%{pkgname})
Requires:       crate(rustcrypto-ff-0.14.0-rc.0) >= 0.14.0-rc.0
Provides:       crate(%{pkgname}/ff)

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "group"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand-core)
Requires:       crate(rustcrypto-group-0.14.0-rc.0) >= 0.14.0-rc.0
Provides:       crate(%{pkgname}/group)

%description -n %{name}+group
This metapackage enables feature "group" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group-bits
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "group-bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/group)
Requires:       crate(rustcrypto-ff-0.14.0-rc.0/bits) >= 0.14.0-rc.0
Provides:       crate(%{pkgname}/group-bits)

%description -n %{name}+group-bits
This metapackage enables feature "group-bits" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure-Rust implementation of group operations on ristretto255 and Curve25519 - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust curve25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
