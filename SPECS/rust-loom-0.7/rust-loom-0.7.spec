# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name loom
%global full_version 0.7.2
%global pkgname loom-0.7

Name:           rust-loom-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "loom"
License:        MIT
URL:            https://github.com/tokio-rs/loom
#!RemoteAsset:  sha256:419e0dc8046cb947daa77eb95ae174acfbddb7673b4151f56d1eed8e93fbfaca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(generator-0.8/default) >= 0.8.1
Requires:       crate(scoped-tls-1/default) >= 1.0.0
Requires:       crate(tracing-0.1/std) >= 0.1.27
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.8
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.8
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "loom"

%package     -n %{name}+checkpoint
Summary:        Permutation testing for concurrent code - feature "checkpoint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/checkpoint) = %{version}

%description -n %{name}+checkpoint
This metapackage enables feature "checkpoint" for the Rust loom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-utils
Summary:        Permutation testing for concurrent code - feature "pin-utils" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-utils-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/pin-utils) = %{version}

%description -n %{name}+pin-utils
This metapackage enables feature "pin-utils" for the Rust loom crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "futures" feature.

%package     -n %{name}+serde
Summary:        Permutation testing for concurrent code - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.92
Requires:       crate(serde-1/derive) >= 1.0.92
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust loom crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Permutation testing for concurrent code - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.33
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust loom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
