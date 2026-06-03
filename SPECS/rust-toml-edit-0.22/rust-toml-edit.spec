# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_edit
%global full_version 0.22.27
%global pkgname toml-edit-0.22

Name:           rust-toml-edit-0.22
Version:        0.22.27
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:41fe8c660ae4257887cf66394862d21dbca4a6ddd26f04a3560410406a2f819a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2.0/default) >= 2.10.0
Requires:       crate(indexmap-2.0/std) >= 2.10.0
Requires:       crate(toml-datetime-0.6/default) >= 0.6.11
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unbounded)

%description
Source code for takopackized Rust crate "toml_edit"

%package     -n %{name}+parse
Summary:        Yet another format-preserving TOML parser - feature "parse"
Requires:       crate(%{pkgname})
Requires:       crate(winnow-0.7/default) >= 0.7.12
Provides:       crate(%{pkgname}/parse)

%description -n %{name}+parse
This metapackage enables feature "parse" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Yet another format-preserving TOML parser - feature "perf"
Requires:       crate(%{pkgname})
Requires:       crate(kstring-2.0/default) >= 2.0.0
Requires:       crate(kstring-2.0/max-inline) >= 2.0.0
Provides:       crate(%{pkgname}/perf)

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-debug
Summary:        Yet another format-preserving TOML parser - feature "unstable-debug"
Requires:       crate(%{pkgname})
Requires:       crate(winnow-0.7/debug) >= 0.7.12
Provides:       crate(%{pkgname}/unstable-debug)

%description -n %{name}+unstable-debug
This metapackage enables feature "unstable-debug" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
