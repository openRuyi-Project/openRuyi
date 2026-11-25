# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name md-5
%global full_version 0.11.0
%global pkgname md-5-0.11

Name:           rust-md-5-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "md-5"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:69b6441f590336821bb897fb28fc622898ccceb1d6cea3fde5ea86b090c4de98
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(digest-0.11/default) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "md-5"

%package     -n %{name}+alloc
Summary:        MD5 hash function - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/alloc) >= 0.11.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust md-5 crate, by pulling
in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        MD5 hash function - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/oid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust md-5 crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        MD5 hash function - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust md-5 crate, by pulling
in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        MD5 hash function - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/zeroize) >= 0.11.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust md-5 crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
