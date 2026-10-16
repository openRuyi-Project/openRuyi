# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yaml-rust2
%global full_version 0.9.0
%global pkgname yaml-rust2-0.9

Name:           rust-yaml-rust2-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "yaml-rust2"
License:        MIT OR Apache-2.0
URL:            https://github.com/Ethiraric/yaml-rust2
#!RemoteAsset:  sha256:2a1a1c0bc9823338a3bdf8c61f994f23ac004c6fa32c08cd152984499b445e8d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arraydeque-0.5/default) >= 0.5.1
Requires:       crate(hashlink-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug-prints) = %{version}

%description
Source code for takopackized Rust crate "yaml-rust2"

%package     -n %{name}+encoding
Summary:        Fully YAML 1.2 compliant YAML parser - feature "encoding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.33
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/encoding) = %{version}

%description -n %{name}+encoding
This metapackage enables feature "encoding" for the Rust yaml-rust2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
