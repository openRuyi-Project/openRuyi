# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auditable-info
%global full_version 0.6.2
%global pkgname auditable-info-0.6

Name:           rust-auditable-info-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "auditable-info"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-secure-code/cargo-auditable
#!RemoteAsset:  sha256:158d56117c834b6e90edbe4c5b5caaefff0996eebe8b952108a0a491330344ee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(auditable-extract-0.3/default) >= 0.3.0
Requires:       crate(miniz-oxide-0.6/default) >= 0.6.2
Requires:       crate(miniz-oxide-0.6/std) >= 0.6.2

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "auditable-info"

%package     -n %{name}+auditable-serde
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "auditable-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(auditable-serde-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/auditable-serde) = %{version}

%description -n %{name}+auditable-serde
This metapackage enables feature "auditable-serde" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/auditable-serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+serde-json
Summary:        High-level crate to extract the dependency trees embedded in binaries by `cargo auditable` - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.57
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust auditable-info crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
