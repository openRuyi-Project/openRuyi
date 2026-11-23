# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path_abs
%global full_version 0.5.1
%global pkgname path-abs-0.5

Name:           rust-path-abs-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "path_abs"
License:        MIT OR Apache-2.0
URL:            https://github.com/vitiral/path_abs
#!RemoteAsset:  sha256:05ef02f6342ac01d8a93b65f96db53fe68a92a15f41144f97fb00a9e669633c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(std-prelude-0.2/default) >= 0.2.12

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "path_abs"

%package     -n %{name}+serde
Summary:        Ergonomic paths and files in rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust path_abs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Ergonomic paths and files in rust - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust path_abs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Ergonomic paths and files in rust - feature "serialize" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Requires:       crate(%{pkgname}/stfu8) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust path_abs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+stfu8
Summary:        Ergonomic paths and files in rust - feature "stfu8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stfu8-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/stfu8) = %{version}

%description -n %{name}+stfu8
This metapackage enables feature "stfu8" for the Rust path_abs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
