# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_edit
%global full_version 0.18.1
%global pkgname toml-edit-0.18

Name:           rust-toml-edit-0.18
Version:        0.18.1
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/ordian/toml_edit
#!RemoteAsset:  sha256:56c59d8dd7d0dcbc6428bf7aa2f0e823e26e43b3c9aca15bbc9475d23e5fa12b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-1/default) >= 1.9.1
Requires:       crate(nom8-0.2/default) >= 0.2.0
Requires:       crate(toml-datetime-0.5/default) >= 0.5.1

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
Summary:        Yet another format-preserving TOML parser - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-spanned-0.6/default) >= 0.6.0
Requires:       crate(serde-spanned-0.6/serde) >= 0.6.0
Requires:       crate(toml-datetime-0.5/serde) >= 0.5.1
Provides:       crate(%{pkgname}/easy) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "easy" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
