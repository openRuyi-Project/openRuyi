# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519-dalek
%global full_version 3.0.0-pre.6
%global pkgname ed25519-dalek-3.0.0-pre.6

Name:           rust-ed25519-dalek-3.0.0-pre.6
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "ed25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:053618a4c3d3bc24f188aa660ae75a46eeab74ef07fb415c61431e5e7cd4749b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curve25519-dalek-5.0.0-pre.6/digest) >= 5.0.0-pre.6
Requires:       crate(ed25519-3.0.0-rc.4) >= 3.0.0-rc.4
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(ed25519-dalek) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "ed25519-dalek"

%package     -n %{name}+alloc
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(curve25519-dalek-5.0.0-pre.6/alloc) >= 5.0.0-pre.6
Requires:       crate(curve25519-dalek-5.0.0-pre.6/digest) >= 5.0.0-pre.6
Requires:       crate(ed25519-3.0.0-rc.4/alloc) >= 3.0.0-rc.4
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(signature-3.0/alloc) >= 3.0.0
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+batch
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "batch"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/rand-core)
Requires:       crate(keccak-0.2.0-rc.1) >= 0.2.0-rc.1
Provides:       crate(%{pkgname}/batch)

%description -n %{name}+batch
This metapackage enables feature "batch" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fast)
Requires:       crate(%{pkgname}/zeroize)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(signature-3.0/digest) >= 3.0.0
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "fast"
Requires:       crate(%{pkgname})
Requires:       crate(curve25519-dalek-5.0.0-pre.6/digest) >= 5.0.0-pre.6
Requires:       crate(curve25519-dalek-5.0.0-pre.6/precomputed-tables) >= 5.0.0-pre.6
Provides:       crate(%{pkgname}/fast)

%description -n %{name}+fast
This metapackage enables feature "fast" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy-compatibility
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "legacy_compatibility"
Requires:       crate(%{pkgname})
Requires:       crate(curve25519-dalek-5.0.0-pre.6/digest) >= 5.0.0-pre.6
Requires:       crate(curve25519-dalek-5.0.0-pre.6/legacy-compatibility) >= 5.0.0-pre.6
Provides:       crate(%{pkgname}/legacy-compatibility)

%description -n %{name}+legacy-compatibility
This metapackage enables feature "legacy_compatibility" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(ed25519-3.0.0-rc.4/pem) >= 3.0.0-rc.4
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(ed25519-3.0.0-rc.4/pkcs8) >= 3.0.0-rc.4
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.10) >= 0.10.1
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(ed25519-3.0.0-rc.4/serde) >= 3.0.0-rc.4
Requires:       crate(serde-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "signature"
Requires:       crate(%{pkgname})
Requires:       crate(signature-3.0) >= 3.0.0
Provides:       crate(%{pkgname}/signature)

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(curve25519-dalek-5.0.0-pre.6/digest) >= 5.0.0-pre.6
Requires:       crate(curve25519-dalek-5.0.0-pre.6/zeroize) >= 5.0.0-pre.6
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
