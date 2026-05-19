# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-dedot
%global full_version 3.1.1
%global pkgname path-dedot-3.0

Name:           rust-path-dedot-3.0
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "path-dedot"
License:        MIT
URL:            https://magiclen.org/path-dedot
#!RemoteAsset:  sha256:07ba0ad7e047712414213ff67533e6dd477af0a4e1d14fb52343e53d30ea9397
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0/default) >= 1.21.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/once-cell-cache)
Provides:       crate(%{pkgname}/unsafe-cache)
Provides:       crate(%{pkgname}/use-unix-paths-on-wasm)

%description
Source code for takopackized Rust crate "path-dedot"

%package     -n %{name}+lazy-static
Summary:        Extending `Path` and `PathBuf` in order to parse the path which contains dots - feature "lazy_static" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/default) >= 1.4
Provides:       crate(%{pkgname}/lazy-static)
Provides:       crate(%{pkgname}/lazy-static-cache)

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust path-dedot crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "lazy_static_cache" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
