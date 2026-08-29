# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_edit
%global full_version 0.20.2
%global pkgname toml-edit-0.20

Name:           rust-toml-edit-0.20
Version:        0.20.2
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:396e4d48bbb2b7554c944bde63101b5ae446cff6ec4a24227428f15eb72ef338
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Requires:       crate(toml-datetime-0.6/default) >= 0.6.3
Requires:       crate(winnow-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unbounded) = %{version}

%description
Source code for takopackized Rust crate "toml_edit"

%package     -n %{name}+perf
Summary:        Yet another format-preserving TOML parser - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kstring-2/default) >= 2.0.0
Requires:       crate(kstring-2/max-inline) >= 2.0.0
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Yet another format-preserving TOML parser - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-spanned-0.6/default) >= 0.6.3
Requires:       crate(serde-spanned-0.6/serde) >= 0.6.3
Requires:       crate(toml-datetime-0.6/serde) >= 0.6.3
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
