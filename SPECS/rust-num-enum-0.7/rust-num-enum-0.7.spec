# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_enum
%global full_version 0.7.6
%global pkgname num-enum-0.7

Name:           rust-num-enum-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "num_enum"
License:        BSD-3-Clause OR MIT OR Apache-2.0
URL:            https://github.com/illicitonion/num_enum
#!RemoteAsset:  sha256:5d0bca838442ec211fa11de3a8b0e0e8f3a4522575b5c4c06ed722e005036f26
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-enum-derive-0.7) >= 0.7.6
Requires:       crate(rustversion-1/default) >= 1.0.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/external-doc) = %{version}

%description
Source code for takopackized Rust crate "num_enum"

%package     -n %{name}+complex-expressions
Summary:        Procedural macros to make inter-operation between primitives and enums easier - feature "complex-expressions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-enum-derive-0.7/complex-expressions) >= 0.7.6
Provides:       crate(%{pkgname}/complex-expressions) = %{version}

%description -n %{name}+complex-expressions
This metapackage enables feature "complex-expressions" for the Rust num_enum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Procedural macros to make inter-operation between primitives and enums easier - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-enum-derive-0.7/std) >= 0.7.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num_enum crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
