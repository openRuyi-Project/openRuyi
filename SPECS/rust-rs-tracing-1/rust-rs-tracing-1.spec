# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rs_tracing
%global full_version 1.1.0
%global pkgname rs-tracing-1

Name:           rust-rs-tracing-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "rs_tracing"
License:        MIT
URL:            https://github.com/andjo403/rs_tracing.git
#!RemoteAsset:  sha256:e3b121670da627e1c0110e7972c9db150dd7f8704dc073cce32c3db9cb7861e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rs_tracing"

%package     -n %{name}+rs-tracing
Summary:        Trace events in the trace event format - feature "rs_tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/rs-tracing) = %{version}

%description -n %{name}+rs-tracing
This metapackage enables feature "rs_tracing" for the Rust rs_tracing crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Trace events in the trace event format - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rs_tracing crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Trace events in the trace event format - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust rs_tracing crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
