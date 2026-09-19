# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lcms2-sys
%global full_version 4.0.7
%global pkgname lcms2-sys-4

Name:           rust-lcms2-sys-4
Version:        4.0.7
Release:        %autorelease
Summary:        Rust crate "lcms2-sys"
License:        MIT
URL:            https://lib.rs/crates/lcms2-sys
#!RemoteAsset:  sha256:264db0b78119c5a37d78bb41fb355daab29b3b29430b53cd92e3da51f0ab06cc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dunce-1) >= 1.0.2
Requires:       crate(libc-0.2/default) >= 0.2.129

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/lcms2-strict-cgats) = %{version}

%description
See lcms2 crate for a safe Rust wrapper.
Source code for takopackized Rust crate "lcms2-sys"

%package     -n %{name}+default
Summary:        Bindings for liblcms2 (Little CMS) with support for Linux, macOS, and Windows - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dynamic) = %{version}
Requires:       crate(%{pkgname}/parallel) = %{version}
Requires:       crate(%{pkgname}/static-fallback) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
See lcms2 crate for a safe Rust wrapper.
This metapackage enables feature "default" for the Rust lcms2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dynamic
Summary:        Bindings for liblcms2 (Little CMS) with support for Linux, macOS, and Windows - feature "dynamic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.25
Provides:       crate(%{pkgname}/dynamic) = %{version}

%description -n %{name}+dynamic
See lcms2 crate for a safe Rust wrapper.
This metapackage enables feature "dynamic" for the Rust lcms2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Bindings for liblcms2 (Little CMS) with support for Linux, macOS, and Windows - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/parallel) >= 1.1.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
See lcms2 crate for a safe Rust wrapper.
This metapackage enables feature "parallel" for the Rust lcms2-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Bindings for liblcms2 (Little CMS) with support for Linux, macOS, and Windows - feature "static" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/static) = %{version}
Provides:       crate(%{pkgname}/static-fallback) = %{version}

%description -n %{name}+static
See lcms2 crate for a safe Rust wrapper.
This metapackage enables feature "static" for the Rust lcms2-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "static-fallback" feature.

%files
%license vendor/LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
