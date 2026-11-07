# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yaml-rust
%global full_version 0.3.5
%global pkgname yaml-rust-0.3

Name:           rust-yaml-rust-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "yaml-rust"
License:        MIT OR Apache-2.0
URL:            http://chyh1990.github.io/yaml-rust/
#!RemoteAsset:  sha256:e66366e18dc58b46801afbf2ca7661a9f59cc8c5962c29892b6039b4f86fa992
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Specify-a-concrete-compatible-Clippy-dependency.patch

%description
Source code for takopackized Rust crate "yaml-rust"

%package     -n %{name}+clippy
Summary:        Missing YAML 1.2 parser for rust - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.166/default) >= 0.0.166
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust yaml-rust crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linked-hash-map
Summary:        Missing YAML 1.2 parser for rust - feature "linked-hash-map" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linked-hash-map-0.0.9/default) >= 0.0.9
Provides:       crate(%{pkgname}/linked-hash-map) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+linked-hash-map
This metapackage enables feature "linked-hash-map" for the Rust yaml-rust crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
