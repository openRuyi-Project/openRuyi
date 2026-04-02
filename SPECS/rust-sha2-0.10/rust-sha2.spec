# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha2
%global full_version 0.10.9
%global pkgname sha2-0.10

Name:           rust-sha2-0.10
Version:        0.10.9
Release:        %autorelease
Summary:        Rust crate "sha2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:a7507d819769d01a365ab707794a4084392c824f54a7a6a7862f8c3d0892b283
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(cpufeatures-0.2/default) >= 0.2.17
Requires:       crate(digest-0.10/default) >= 0.10.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/compress)
Provides:       crate(%{pkgname}/force-soft)
Provides:       crate(%{pkgname}/force-soft-compact)
Provides:       crate(%{pkgname}/loongarch64-asm)

%description
Source code for takopackized Rust crate "sha2"

%package     -n %{name}+oid
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/oid) >= 0.10.7
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2-asm
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "sha2-asm" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(sha2-asm-0.6/default) >= 0.6.1
Provides:       crate(%{pkgname}/asm)
Provides:       crate(%{pkgname}/asm-aarch64)
Provides:       crate(%{pkgname}/sha2-asm)

%description -n %{name}+sha2-asm
This metapackage enables feature "sha2-asm" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "asm", and "asm-aarch64" features.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/std) >= 0.10.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
