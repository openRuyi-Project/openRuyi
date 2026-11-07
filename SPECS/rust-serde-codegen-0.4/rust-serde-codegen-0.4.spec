# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_codegen
%global full_version 0.4.3
%global pkgname serde-codegen-0.4

Name:           rust-serde-codegen-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "serde_codegen"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-serde
#!RemoteAsset:  sha256:78039c094484c3f82dd91717644aa922f5372c8ca24b876cc4c8028d377cc704
Source:         https://static.crates.io/crates/serde_codegen/0.4.3/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aster-0.3) >= 0.3.3
Requires:       crate(quasi-0.3) >= 0.3.1

Provides:       crate(%{pkgname}) = %{version}
Patch2000:      2000-Correct-dependency-metadata-for-the-Serde-0.4-generator.patch

%description
Source code for takopackized Rust crate "serde_codegen"

%package     -n %{name}+quasi-codegen
Summary:        Macros to auto-generate implementations for the serde framework - feature "quasi_codegen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quasi-codegen-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/quasi-codegen) = %{version}

%description -n %{name}+quasi-codegen
This metapackage enables feature "quasi_codegen" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quasi-macros
Summary:        Macros to auto-generate implementations for the serde framework - feature "quasi_macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quasi-macros-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/quasi-macros) = %{version}

%description -n %{name}+quasi-macros
This metapackage enables feature "quasi_macros" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly" feature.

%package     -n %{name}+syntex
Summary:        Macros to auto-generate implementations for the serde framework - feature "syntex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/syntex) = %{version}

%description -n %{name}+syntex
This metapackage enables feature "syntex" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Macros to auto-generate implementations for the serde framework - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        Macros to auto-generate implementations for the serde framework - feature "with-syntex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syntex) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Requires:       crate(quasi-0.3/with-syntex) >= 0.3.1
Requires:       crate(quasi-codegen-0.3/with-syntex) >= 0.3.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
This metapackage enables feature "with-syntex" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
