# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519-dalek
%global full_version 3.0.0-rc.1
%global pkgname ed25519-dalek-3.0.0-rc.1

Name:           rust-ed25519-dalek-3.0.0-rc.1
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "ed25519-dalek"
License:        BSD-3-Clause
URL:            https://github.com/dalek-cryptography/curve25519-dalek
#!RemoteAsset:  sha256:1685663e23882cd8517dcbcb1c23a6ebff4433c22dfb681d760219b62cd1b849
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curve25519-dalek-5.0.0-rc.1/digest) >= 5.0.0-rc.1
Requires:       crate(ed25519-3) >= 3.0.0
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(subtle-2) >= 2.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "ed25519-dalek"

%package     -n %{name}+alloc
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-5.0.0-rc.1/alloc) >= 5.0.0-rc.1
Requires:       crate(curve25519-dalek-5.0.0-rc.1/digest) >= 5.0.0-rc.1
Requires:       crate(ed25519-3/alloc) >= 3.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(signature-3/alloc) >= 3.0.0
Requires:       crate(zeroize-1/alloc) >= 1.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+batch
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "batch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(%{pkgname}/strobe-rs) = %{version}
Requires:       crate(keccak-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/batch) = %{version}

%description -n %{name}+batch
This metapackage enables feature "batch" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fast) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-3/digest) >= 3.0.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "fast"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-5.0.0-rc.1/digest) >= 5.0.0-rc.1
Requires:       crate(curve25519-dalek-5.0.0-rc.1/precomputed-tables) >= 5.0.0-rc.1
Provides:       crate(%{pkgname}/fast) = %{version}

%description -n %{name}+fast
This metapackage enables feature "fast" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy-compatibility
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "legacy_compatibility"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-5.0.0-rc.1/digest) >= 5.0.0-rc.1
Requires:       crate(curve25519-dalek-5.0.0-rc.1/legacy-compatibility) >= 5.0.0-rc.1
Provides:       crate(%{pkgname}/legacy-compatibility) = %{version}

%description -n %{name}+legacy-compatibility
This metapackage enables feature "legacy_compatibility" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(ed25519-3/pem) >= 3.0.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-3/pkcs8) >= 3.0.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-3/serde) >= 3.0.0
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-3) >= 3.0.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strobe-rs
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "strobe-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strobe-rs-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/strobe-rs) = %{version}

%description -n %{name}+strobe-rs
This metapackage enables feature "strobe-rs" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verification in pure Rust - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curve25519-dalek-5.0.0-rc.1/digest) >= 5.0.0-rc.1
Requires:       crate(curve25519-dalek-5.0.0-rc.1/zeroize) >= 5.0.0-rc.1
Requires:       crate(zeroize-1) >= 1.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ed25519-dalek crate, by pulling in any additional dependencies needed by that feature.

# Use the complete Cargo version so the release and RC can coexist.
%install -a
mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
   "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
