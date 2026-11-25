# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name des
%global full_version 0.9.0
%global pkgname des-0.9

Name:           rust-des-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "des"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:916a94e407b54f9034d71dd748234cd1e516ced6284009906ae246f177eafe5a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "des"

%package     -n %{name}+zeroize
Summary:        DES and Triple DES (3DES, TDES) block ciphers implementation - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/zeroize) >= 0.5.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust des crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
