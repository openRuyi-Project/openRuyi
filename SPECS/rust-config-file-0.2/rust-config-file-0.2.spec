# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name config-file
%global full_version 0.2.3
%global pkgname config-file-0.2

Name:           rust-config-file-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "config-file"
License:        BSD-2-Clause
URL:            https://github.com/Keruspe/config-file
#!RemoteAsset:  sha256:df51e72c150781d2c7d4cbcb0b803277caaa80476786994a62961a8f1010dafb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "config-file"

%package     -n %{name}+serde-xml-rs
Summary:        Read and parse configuration file automatically - feature "serde-xml-rs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-xml-rs-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/serde-xml-rs) = %{version}
Provides:       crate(%{pkgname}/xml) = %{version}

%description -n %{name}+serde-xml-rs
This metapackage enables feature "serde-xml-rs" for the Rust config-file crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xml" feature.

%package     -n %{name}+serde-json
Summary:        Read and parse configuration file automatically - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust config-file crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+serde-yaml
Summary:        Read and parse configuration file automatically - feature "serde_yaml" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-yaml-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/serde-yaml) = %{version}
Provides:       crate(%{pkgname}/yaml) = %{version}

%description -n %{name}+serde-yaml
This metapackage enables feature "serde_yaml" for the Rust config-file crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "yaml" feature.

%package     -n %{name}+toml-crate
Summary:        Read and parse configuration file automatically - feature "toml-crate" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/toml) = %{version}
Provides:       crate(%{pkgname}/toml-crate) = %{version}

%description -n %{name}+toml-crate
This metapackage enables feature "toml-crate" for the Rust config-file crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "toml" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
