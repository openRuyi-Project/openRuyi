# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1
%global full_version 0.10.6
%global pkgname sha1-0.10

Name:           rust-sha1-0.10
Version:        0.10.6
Release:        %autorelease
Summary:        Rust crate "sha1"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:e3bf829a2d51ab4a5ddf1352d8470c140cadc8301b2ae1789db023f01cedd6ba
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
Provides:       crate(%{pkgname}/loongarch64-asm)

%description
Source code for takopackized Rust crate "sha1"

%package     -n %{name}+oid
Summary:        SHA-1 hash function - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/oid) >= 0.10.7
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1-asm
Summary:        SHA-1 hash function - feature "sha1-asm" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(sha1-asm-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/asm)
Provides:       crate(%{pkgname}/sha1-asm)

%description -n %{name}+sha1-asm
This metapackage enables feature "sha1-asm" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "asm" feature.

%package     -n %{name}+std
Summary:        SHA-1 hash function - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/std) >= 0.10.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
