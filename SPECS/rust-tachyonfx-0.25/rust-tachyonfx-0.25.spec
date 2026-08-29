# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tachyonfx
%global full_version 0.25.0
%global pkgname tachyonfx-0.25

Name:           rust-tachyonfx-0.25
Version:        0.25.0
Release:        %autorelease
Summary:        Rust crate "tachyonfx"
License:        MIT
URL:            https://github.com/ratatui/tachyonfx
#!RemoteAsset:  sha256:c144c687e9f3628c06add1b6db585a68d3cd285a9d7213b9bca836771e337592
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bon-3) >= 3.8.2
Requires:       crate(compact-str-0.9) >= 0.9.0
Requires:       crate(micromath-2/default) >= 2.1.0
Requires:       crate(ratatui-core-0.1) >= 0.1.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/sendable) = %{version}

%description
Source code for takopackized Rust crate "tachyonfx"

%package     -n %{name}+default
Summary:        Ratatui library for creating shader-like effects in TUIs - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dsl) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tachyonfx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dsl
Summary:        Ratatui library for creating shader-like effects in TUIs - feature "dsl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anpa-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/dsl) = %{version}

%description -n %{name}+dsl
This metapackage enables feature "dsl" for the Rust tachyonfx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Ratatui library for creating shader-like effects in TUIs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bon-3/std) >= 3.8.2
Requires:       crate(compact-str-0.9/std) >= 0.9.0
Requires:       crate(ratatui-core-0.1/std) >= 0.1.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/std-duration) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tachyonfx crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std-duration" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
