# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-absolutize
%global full_version 3.1.1
%global pkgname path-absolutize-3.0

Name:           rust-path-absolutize-3.0
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "path-absolutize"
License:        MIT
URL:            https://magiclen.org/path-absolutize
#!RemoteAsset:  sha256:e4af381fe79fa195b4909485d99f73a80792331df0625188e707854f0b3383f5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(path-dedot-3.0/default) >= 3.1.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "path-absolutize"

%package     -n %{name}+lazy-static-cache
Summary:        Extending `Path` and `PathBuf` in order to get an absolute path and remove the containing dots - feature "lazy_static_cache"
Requires:       crate(%{pkgname})
Requires:       crate(path-dedot-3.0/lazy-static-cache) >= 3.1.1
Provides:       crate(%{pkgname}/lazy-static-cache)

%description -n %{name}+lazy-static-cache
This metapackage enables feature "lazy_static_cache" for the Rust path-absolutize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell-cache
Summary:        Extending `Path` and `PathBuf` in order to get an absolute path and remove the containing dots - feature "once_cell_cache"
Requires:       crate(%{pkgname})
Requires:       crate(path-dedot-3.0/once-cell-cache) >= 3.1.1
Provides:       crate(%{pkgname}/once-cell-cache)

%description -n %{name}+once-cell-cache
This metapackage enables feature "once_cell_cache" for the Rust path-absolutize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unsafe-cache
Summary:        Extending `Path` and `PathBuf` in order to get an absolute path and remove the containing dots - feature "unsafe_cache"
Requires:       crate(%{pkgname})
Requires:       crate(path-dedot-3.0/unsafe-cache) >= 3.1.1
Provides:       crate(%{pkgname}/unsafe-cache)

%description -n %{name}+unsafe-cache
This metapackage enables feature "unsafe_cache" for the Rust path-absolutize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-unix-paths-on-wasm
Summary:        Extending `Path` and `PathBuf` in order to get an absolute path and remove the containing dots - feature "use_unix_paths_on_wasm"
Requires:       crate(%{pkgname})
Requires:       crate(path-dedot-3.0/use-unix-paths-on-wasm) >= 3.1.1
Provides:       crate(%{pkgname}/use-unix-paths-on-wasm)

%description -n %{name}+use-unix-paths-on-wasm
This metapackage enables feature "use_unix_paths_on_wasm" for the Rust path-absolutize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
