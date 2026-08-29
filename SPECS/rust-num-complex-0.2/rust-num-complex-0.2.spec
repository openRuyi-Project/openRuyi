# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-complex
%global full_version 0.2.4
%global pkgname num-complex-0.2

Name:           rust-num-complex-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "num-complex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-complex
#!RemoteAsset:  sha256:b6b19411a9719e753aff12e5187b74d60d3dc449ec3f4dc21e3989c3f554bc95
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(num-traits-0.2) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-complex"

%package     -n %{name}+i128
Summary:        Complex numbers implementation for Rust - feature "i128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/i128) >= 0.2.11
Provides:       crate(%{pkgname}/i128) = %{version}

%description -n %{name}+i128
This metapackage enables feature "i128" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Complex numbers implementation for Rust - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Complex numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Complex numbers implementation for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.11
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
