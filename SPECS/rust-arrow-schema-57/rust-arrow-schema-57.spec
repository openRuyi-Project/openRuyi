# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-schema
%global full_version 57.3.1
%global pkgname arrow-schema-57

Name:           rust-arrow-schema-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-schema"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:e4cf0d4a6609679e03002167a61074a21d7b1ad9ea65e462b2c0a97f8a3b2bc6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-schema"

%package     -n %{name}+bitflags
Summary:        Defines the logical types for arrow arrays - feature "bitflags" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.0.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust arrow-schema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ffi" feature.

%package     -n %{name}+canonical-extension-types
Summary:        Defines the logical types for arrow arrays - feature "canonical_extension_types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/rc) >= 1.0.0
Requires:       crate(serde-core-1/std) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/canonical-extension-types) = %{version}

%description -n %{name}+canonical-extension-types
This metapackage enables feature "canonical_extension_types" for the Rust arrow-schema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Defines the logical types for arrow arrays - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-core-1/rc) >= 1.0.0
Requires:       crate(serde-core-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust arrow-schema crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
