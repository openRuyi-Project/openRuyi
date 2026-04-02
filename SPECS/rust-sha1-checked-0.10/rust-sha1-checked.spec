# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1-checked
%global full_version 0.10.0
%global pkgname sha1-checked-0.10

Name:           rust-sha1-checked-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "sha1-checked"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:89f599ac0c323ebb1c6082821a54962b839832b03984598375bff3975b804423
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.7
Requires:       crate(sha1-0.10/compress) >= 0.10.6
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "sha1-checked"

%package     -n %{name}+default
Summary:        SHA-1 hash function with collision detection - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/oid)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha1-checked crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        SHA-1 hash function with collision detection - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/oid) >= 0.10.7
Requires:       crate(sha1-0.10/compress) >= 0.10.6
Requires:       crate(sha1-0.10/oid) >= 0.10.6
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha1-checked crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        SHA-1 hash function with collision detection - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/std) >= 0.10.7
Requires:       crate(sha1-0.10/compress) >= 0.10.6
Requires:       crate(sha1-0.10/std) >= 0.10.6
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha1-checked crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        SHA-1 hash function with collision detection - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.7
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha1-checked crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
