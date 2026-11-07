# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-complex
%global full_version 0.1.44
%global pkgname num-complex-0.1

Name:           rust-num-complex-0.1
Version:        0.1.44
Release:        %autorelease
Summary:        Rust crate "num-complex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-complex
#!RemoteAsset:  sha256:17cf384bef067563c44d41028840dbecc7f06f2aa5d7881a81dfb0fc7c72f202
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.4.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "num-complex"

%package     -n %{name}+rustc-serialize
Summary:        Complex numbers implementation for Rust - feature "rustc-serialize" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc-serialize) = %{version}

%description -n %{name}+rustc-serialize
This metapackage enables feature "rustc-serialize" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+serde
Summary:        Complex numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
