# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cmac
%global full_version 0.7.2
%global pkgname cmac-0.7

Name:           rust-cmac-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "cmac"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/MACs
#!RemoteAsset:  sha256:8543454e3c3f5126effff9cd44d562af4e31fb8ce1cc0d3dcd8f084515dbc1aa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.4/default) >= 0.4.2
Requires:       crate(dbl-0.3/default) >= 0.3.0
Requires:       crate(digest-0.10/default) >= 0.10.3
Requires:       crate(digest-0.10/mac) >= 0.10.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cmac"

%package     -n %{name}+std
Summary:        Generic implementation of Cipher-based Message Authentication Code - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/mac) >= 0.10.3
Requires:       crate(digest-0.10/std) >= 0.10.3
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust cmac crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Generic implementation of Cipher-based Message Authentication Code - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/zeroize) >= 0.4.2
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust cmac crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
