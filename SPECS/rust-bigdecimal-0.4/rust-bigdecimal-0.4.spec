# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bigdecimal
%global full_version 0.4.10
%global pkgname bigdecimal-0.4

Name:           rust-bigdecimal-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "bigdecimal"
License:        MIT OR Apache-2.0
URL:            https://github.com/akubera/bigdecimal-rs
#!RemoteAsset:  sha256:4d6867f1565b3aad85681f1015055b087fcfd840d6aeee6eee7f2da317603695
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(libm-0.2/default) >= 0.2.6
Requires:       crate(num-bigint-0.4) >= 0.4.0
Requires:       crate(num-integer-0.1) >= 0.1.0
Requires:       crate(num-traits-0.2) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/string-only) = %{version}

%description
Source code for takopackized Rust crate "bigdecimal"

%package     -n %{name}+serde
Summary:        Arbitrary precision decimal numbers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bigdecimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Arbitrary precision decimal numbers - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/alloc) >= 1.0.0
Requires:       crate(serde-json-1/arbitrary-precision) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust bigdecimal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Arbitrary precision decimal numbers - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/std) >= 0.4.0
Requires:       crate(num-integer-0.1/std) >= 0.1.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bigdecimal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
