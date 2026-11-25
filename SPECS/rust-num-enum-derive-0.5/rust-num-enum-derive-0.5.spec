# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_enum_derive
%global full_version 0.5.11
%global pkgname num-enum-derive-0.5

Name:           rust-num-enum-derive-0.5
Version:        0.5.11
Release:        %autorelease
Summary:        Rust crate "num_enum_derive"
License:        BSD-3-Clause OR MIT OR Apache-2.0
URL:            https://github.com/illicitonion/num_enum
#!RemoteAsset:  sha256:dcbff9bc912032c62bf65ef1d5aea88983b420f4f839db1e9b0c281a25c9c799
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.15
Requires:       crate(syn-1/parsing) >= 1.0.15

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/external-doc) = %{version}

%description
Source code for takopackized Rust crate "num_enum_derive"

%package     -n %{name}+complex-expressions
Summary:        Internal implementation details for ::num_enum (Procedural macros to make inter-operation between primitives and enums easier) - feature "complex-expressions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1/full) >= 1.0.15
Requires:       crate(syn-1/parsing) >= 1.0.15
Provides:       crate(%{pkgname}/complex-expressions) = %{version}

%description -n %{name}+complex-expressions
This metapackage enables feature "complex-expressions" for the Rust num_enum_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-crate
Summary:        Internal implementation details for ::num_enum (Procedural macros to make inter-operation between primitives and enums easier) - feature "proc-macro-crate" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-crate-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proc-macro-crate) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+proc-macro-crate
This metapackage enables feature "proc-macro-crate" for the Rust num_enum_derive crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
