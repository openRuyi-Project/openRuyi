# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yazi-prebuilt
%global full_version 0.1.0
%global pkgname yazi-prebuilt-0.1

Name:           rust-yazi-prebuilt-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "yazi-prebuilt"
License:        MIT
URL:            https://github.com/sxyazi/yazi
#!RemoteAsset:  sha256:33232d9116df6415ddfcdf72701b1b7439ce87f240a14723e8dd5d17e7ed5f98
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "yazi-prebuilt"

%package     -n %{name}+anyhow
Summary:        Used to place the pre-built assets of yazi (https://github.com/sxyazi/yazi) - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust yazi-prebuilt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+build-deps
Summary:        Used to place the pre-built assets of yazi (https://github.com/sxyazi/yazi) - feature "build_deps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/anyhow) = %{version}
Requires:       crate(%{pkgname}/syntect) = %{version}
Requires:       crate(%{pkgname}/walkdir) = %{version}
Provides:       crate(%{pkgname}/build-deps) = %{version}

%description -n %{name}+build-deps
This metapackage enables feature "build_deps" for the Rust yazi-prebuilt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntect
Summary:        Used to place the pre-built assets of yazi (https://github.com/sxyazi/yazi) - feature "syntect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntect-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/syntect) = %{version}

%description -n %{name}+syntect
This metapackage enables feature "syntect" for the Rust yazi-prebuilt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Used to place the pre-built assets of yazi (https://github.com/sxyazi/yazi) - feature "walkdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/walkdir) = %{version}

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust yazi-prebuilt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
