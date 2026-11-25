# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hcl-rs
%global full_version 0.19.8
%global pkgname hcl-rs-0.19

Name:           rust-hcl-rs-0.19
Version:        0.19.8
Release:        %autorelease
Summary:        Rust crate "hcl-rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/martinohmann/hcl-rs
#!RemoteAsset:  sha256:212c6fce17a8b9e0eab43ccf61c8bc5d2c51fc24ad52d19bd1d2be2eeba22d02
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hcl-edit-0.9/default) >= 0.9.7
Requires:       crate(hcl-primitives-0.1/default) >= 0.1.12
Requires:       crate(hcl-primitives-0.1/serde) >= 0.1.12
Requires:       crate(indexmap-2/default) >= 2.7.0
Requires:       crate(indexmap-2/serde) >= 2.7.0
Requires:       crate(itoa-1/default) >= 1.0.14
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(vecmap-rs-0.2/default) >= 0.2.0
Requires:       crate(vecmap-rs-0.2/serde) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hcl-rs"

%package     -n %{name}+perf
Summary:        HCL parser and formatter for rust with serde support - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hcl-edit-0.9/perf) >= 0.9.7
Requires:       crate(hcl-primitives-0.1/perf) >= 0.1.12
Requires:       crate(hcl-primitives-0.1/serde) >= 0.1.12
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust hcl-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
