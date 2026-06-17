# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name keccak
%global full_version 0.2.0
%global pkgname keccak-0.2

Name:           rust-keccak-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "keccak"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/sponges
#!RemoteAsset:  sha256:9e24a010dd405bd7ed803e5253182815b41bf2e6a80cc3bfc066658e03a198aa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "keccak"

%package     -n %{name}+parallel
Summary:        Pure Rust implementation of the Keccak sponge functions - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust keccak crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
