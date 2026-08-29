# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_edit
%global full_version 0.23.10+spec-1.0.0
%global pkgname toml-edit-0.23

Name:           rust-toml-edit-0.23
Version:        0.23.10
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:84c8b9f757e028cee9fa244aea147aab2a9ec09d5325a9b01e0a49730c2b5269
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.11.4
Requires:       crate(indexmap-2/std) >= 2.11.4
Requires:       crate(toml-datetime-0.7/default) >= 0.7.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unbounded) = %{version}

%description
Source code for takopackized Rust crate "toml_edit"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Requires:       crate(anstream-0.6/default) >= 0.6.20
Requires:       crate(anstyle-1/default) >= 1.0.11
Requires:       crate(toml-parser-1/debug) >= 1.0.5
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Yet another format-preserving TOML parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Requires:       crate(%{pkgname}/parse) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Yet another format-preserving TOML parser - feature "display"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-writer-1/default) >= 1.0.5
Provides:       crate(%{pkgname}/display) = %{version}

%description -n %{name}+display
This metapackage enables feature "display" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Yet another format-preserving TOML parser - feature "parse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-parser-1/default) >= 1.0.5
Requires:       crate(winnow-0.7/default) >= 0.7.13
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+parse
This metapackage enables feature "parse" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Yet another format-preserving TOML parser - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/default) >= 1.0.225
Requires:       crate(serde-spanned-1/default) >= 1.0.4
Requires:       crate(serde-spanned-1/serde) >= 1.0.4
Requires:       crate(toml-datetime-0.7/serde) >= 0.7.4
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
