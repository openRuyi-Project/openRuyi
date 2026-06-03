# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name md-5
%global full_version 0.10.6
%global pkgname md-5-0.10

Name:           rust-md-5-0.10
Version:        0.10.6
Release:        %autorelease
Summary:        Rust crate "md-5"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:d89e7ee0cfbedfc4da3340218492196241d89eefb6dab27de5df917a6d2e78cf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(digest-0.10/default) >= 0.10.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/force-soft)
Provides:       crate(%{pkgname}/loongarch64-asm)

%description
Source code for takopackized Rust crate "md-5"

%package     -n %{name}+md5-asm
Summary:        MD5 hash function - feature "md5-asm" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(md5-asm-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/asm)
Provides:       crate(%{pkgname}/md5-asm)

%description -n %{name}+md5-asm
This metapackage enables feature "md5-asm" for the Rust md-5 crate.

Additionally, this package also provides the "asm" feature.

%package     -n %{name}+oid
Summary:        MD5 hash function - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/oid) >= 0.10.7
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust md-5 crate.

%package     -n %{name}+std
Summary:        MD5 hash function - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/std) >= 0.10.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust md-5 crate.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
