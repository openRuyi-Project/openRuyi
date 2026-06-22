# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lz4_flex
%global full_version 0.13.1
%global pkgname lz4-flex-0.13

Name:           rust-lz4-flex-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "lz4_flex"
License:        MIT
URL:            https://github.com/pseitz/lz4_flex
#!RemoteAsset:  sha256:7ef0d4ed8669f8f8826eb00dc878084aa8f253506c4fd5e8f58f5bce72ddb97e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/checked-decode) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/safe-decode) = %{version}
Provides:       crate(%{pkgname}/safe-encode) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "lz4_flex"

%package     -n %{name}+default
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/checked-decode) = %{version}
Requires:       crate(%{pkgname}/frame) = %{version}
Requires:       crate(%{pkgname}/safe-decode) = %{version}
Requires:       crate(%{pkgname}/safe-encode) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lz4_flex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+frame
Summary:        Fastest LZ4 implementation in Rust, no unsafe by default - feature "frame"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(twox-hash-2/xxhash32) >= 2.0.0
Provides:       crate(%{pkgname}/frame) = %{version}

%description -n %{name}+frame
This metapackage enables feature "frame" for the Rust lz4_flex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
