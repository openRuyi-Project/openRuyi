# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name slog
%global full_version 2.8.2
%global pkgname slog-2

Name:           rust-slog-2
Version:        2.8.2
Release:        %autorelease
Summary:        Rust crate "slog"
License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://github.com/slog-rs/slog
#!RemoteAsset:  sha256:9b3b8565691b22d2bdfc066426ed48f837fc0c5f2c8cad8d9718f7f99d6995c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1) >= 1.0.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dynamic-keys) = %{version}
Provides:       crate(%{pkgname}/max-level-debug) = %{version}
Provides:       crate(%{pkgname}/max-level-error) = %{version}
Provides:       crate(%{pkgname}/max-level-info) = %{version}
Provides:       crate(%{pkgname}/max-level-off) = %{version}
Provides:       crate(%{pkgname}/max-level-trace) = %{version}
Provides:       crate(%{pkgname}/max-level-warn) = %{version}
Provides:       crate(%{pkgname}/nothreads) = %{version}
Provides:       crate(%{pkgname}/release-max-level-debug) = %{version}
Provides:       crate(%{pkgname}/release-max-level-error) = %{version}
Provides:       crate(%{pkgname}/release-max-level-info) = %{version}
Provides:       crate(%{pkgname}/release-max-level-off) = %{version}
Provides:       crate(%{pkgname}/release-max-level-trace) = %{version}
Provides:       crate(%{pkgname}/release-max-level-warn) = %{version}

%description
Source code for takopackized Rust crate "slog"

%package     -n %{name}+anyhow
Summary:        Structured, extensible, composable logging for Rust - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1) >= 1.0.0
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust slog crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Structured, extensible, composable logging for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nested-values) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust slog crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nested-values
Summary:        Structured, extensible, composable logging for Rust - feature "nested-values"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(erased-serde-0.3/alloc) >= 0.3.0
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/nested-values) = %{version}

%description -n %{name}+nested-values
This metapackage enables feature "nested-values" for the Rust slog crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot-0-12
Summary:        Structured, extensible, composable logging for Rust - feature "parking_lot_0_12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot-0-12) = %{version}

%description -n %{name}+parking-lot-0-12
This metapackage enables feature "parking_lot_0_12" for the Rust slog crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Structured, extensible, composable logging for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/std) >= 1.0.0
Requires:       crate(serde-core-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust slog crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
