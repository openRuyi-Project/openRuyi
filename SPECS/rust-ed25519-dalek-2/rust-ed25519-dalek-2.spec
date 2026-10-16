# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519-dalek
%global full_version 2.2.0
%global pkgname ed25519-dalek-2

Name:           rust-ed25519-dalek-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "ed25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:70e796c081cee67dc755e1a36a0a172b897fab85fc3f6bc48307991f64e4eca9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curve25519-dalek-4/digest) >= 4.0.0
Requires:       crate(ed25519-2) >= 2.2.0
Requires:       crate(sha2-0.10) >= 0.10.0
Requires:       crate(subtle-2) >= 2.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "ed25519-dalek"

%package     -n %{name}+alloc
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/alloc) >= 4.0.0
Requires:       crate(curve25519-dalek-4/digest) >= 4.0.0
Requires:       crate(ed25519-2/alloc) >= 2.2.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(zeroize-1/alloc) >= 1.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+asm
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/asm) >= 0.10.0
Provides:       crate(%{pkgname}/asm) = %{version}

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+batch
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "batch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/merlin) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Provides:       crate(%{pkgname}/batch) = %{version}

%description -n %{name}+batch
This metapackage enables feature "batch" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fast) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-2/digest) >= 2.0.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "fast"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/digest) >= 4.0.0
Requires:       crate(curve25519-dalek-4/precomputed-tables) >= 4.0.0
Provides:       crate(%{pkgname}/fast) = %{version}

%description -n %{name}+fast
This metapackage enables feature "fast" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy-compatibility
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "legacy_compatibility"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/digest) >= 4.0.0
Requires:       crate(curve25519-dalek-4/legacy-compatibility) >= 4.0.0
Provides:       crate(%{pkgname}/legacy-compatibility) = %{version}

%description -n %{name}+legacy-compatibility
This metapackage enables feature "legacy_compatibility" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+merlin
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "merlin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(merlin-3) >= 3.0.0
Provides:       crate(%{pkgname}/merlin) = %{version}

%description -n %{name}+merlin
This metapackage enables feature "merlin" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(ed25519-2/pem) >= 2.2.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-2/pkcs8) >= 2.2.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6) >= 0.6.4
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-2/serde) >= 2.2.0
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-2) >= 2.0.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(ed25519-2/std) >= 2.2.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(sha2-0.10/std) >= 0.10.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-4/digest) >= 4.0.0
Requires:       crate(curve25519-dalek-4/zeroize) >= 4.0.0
Requires:       crate(zeroize-1) >= 1.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
