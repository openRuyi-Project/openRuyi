# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 2.11.0
%global pkgname bitflags-2.0

Name:           rust-bitflags-2.0
Version:        2.11.0
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/bitflags/bitflags
#!RemoteAsset:  sha256:843867be96c8daad0d758b57df9392b6d8d271134fce549de6ce169ff98a92af
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/example-generated)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bitflags"

%package     -n %{name}+arbitrary
Summary:        Macro to generate structures which behave like bitflags - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Macro to generate structures which behave like bitflags - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.12
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-core
Summary:        Macro to generate structures which behave like bitflags - feature "serde_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde-core)

%description -n %{name}+serde-core
This metapackage enables feature "serde_core" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
