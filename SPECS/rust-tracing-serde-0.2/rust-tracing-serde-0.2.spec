# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-serde
%global full_version 0.2.0
%global pkgname tracing-serde-0.2

Name:           rust-tracing-serde-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "tracing-serde"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:704b1aeb7be0d0a84fc9828cae51dab5970fee5088f83d1dd7ee6f6246fc6ff1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(tracing-core-0.1/default) >= 0.1.28
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tracing-serde"

%package     -n %{name}+valuable
Summary:        Compatibility layer for serializing trace data with `serde` - feature "valuable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/valuable-crate) = %{version}
Requires:       crate(%{pkgname}/valuable-serde) = %{version}
Requires:       crate(tracing-core-0.1/valuable) >= 0.1.28
Provides:       crate(%{pkgname}/valuable) = %{version}

%description -n %{name}+valuable
This metapackage enables feature "valuable" for the Rust tracing-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-serde
Summary:        Compatibility layer for serializing trace data with `serde` - feature "valuable-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(valuable-serde-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-serde) = %{version}

%description -n %{name}+valuable-serde
This metapackage enables feature "valuable-serde" for the Rust tracing-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+valuable-crate
Summary:        Compatibility layer for serializing trace data with `serde` - feature "valuable_crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(valuable-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable-crate) = %{version}

%description -n %{name}+valuable-crate
This metapackage enables feature "valuable_crate" for the Rust tracing-serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
