# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name secrecy
%global full_version 0.10.3
%global pkgname secrecy-0.10

Name:           rust-secrecy-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "secrecy"
License:        Apache-2.0 OR MIT
URL:            https://github.com/iqlusioninc/crates/
#!RemoteAsset:  sha256:e891af845473308773346dc847b2c23ee78fe442e0472ac50e22a18a93d3ae5a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zeroize-1/alloc) >= 1.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "secrecy"

%package     -n %{name}+serde
Summary:        Wrapper types and traits for secret management which help ensure they aren't accidentally copied, logged, or otherwise exposed (as much as possible), and also ensure secrets are securely wiped from memory when dropped - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust secrecy crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
