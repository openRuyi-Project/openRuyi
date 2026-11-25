# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hcl-edit
%global full_version 0.9.7
%global pkgname hcl-edit-0.9

Name:           rust-hcl-edit-0.9
Version:        0.9.7
Release:        %autorelease
Summary:        Rust crate "hcl-edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/martinohmann/hcl-rs
#!RemoteAsset:  sha256:8a67cc5751cb5996669b9780cd738d4541a76c2d5f2f10c17af4965c5a03a5f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(hcl-primitives-0.1/default) >= 0.1.12
Requires:       crate(pratt-0.4/default) >= 0.4.0
Requires:       crate(vecmap-rs-0.2/default) >= 0.2.0
Requires:       crate(winnow-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hcl-edit"

%package     -n %{name}+perf
Summary:        Parse and modify HCL while preserving comments and whitespace - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hcl-primitives-0.1/perf) >= 0.1.12
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust hcl-edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
