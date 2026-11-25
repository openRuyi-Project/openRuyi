# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_enum
%global full_version 0.5.11
%global pkgname num-enum-0.5

Name:           rust-num-enum-0.5
Version:        0.5.11
Release:        %autorelease
Summary:        Rust crate "num_enum"
License:        BSD-3-Clause OR MIT OR Apache-2.0
URL:            https://github.com/illicitonion/num_enum
#!RemoteAsset:  sha256:1f646caf906c20226733ed5b1374287eb97e3c2a5c227ce668c1f2ce20ae57c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-enum-derive-0.5) >= 0.5.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/external-doc) = %{version}

%description
Source code for takopackized Rust crate "num_enum"

%package     -n %{name}+complex-expressions
Summary:        Procedural macros to make inter-operation between primitives and enums easier - feature "complex-expressions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-enum-derive-0.5/complex-expressions) >= 0.5.11
Provides:       crate(%{pkgname}/complex-expressions) = %{version}

%description -n %{name}+complex-expressions
This metapackage enables feature "complex-expressions" for the Rust num_enum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Procedural macros to make inter-operation between primitives and enums easier - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-enum-derive-0.5/std) >= 0.5.11
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num_enum crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
