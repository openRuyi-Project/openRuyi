# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libseat
%global full_version 0.2.4
%global pkgname libseat-0.2

Name:           rust-libseat-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "libseat"
License:        MIT
URL:            https://github.com/PolyMeilex/libseat-rs
#!RemoteAsset:  sha256:6656c69b6e0366ffb83faa232f3e4fda5fc91161722d140f2c95ce2e90b1ef31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(errno-0.3/default) >= 0.3.1
Requires:       crate(libseat-sys-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "libseat"

%package     -n %{name}+cc
Summary:        Safe libseat bindings - feature "cc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.68
Provides:       crate(%{pkgname}/cc) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust libseat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+custom-logger
Summary:        Safe libseat bindings - feature "custom_logger" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cc) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Provides:       crate(%{pkgname}/custom-logger) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+custom-logger
This metapackage enables feature "custom_logger" for the Rust libseat crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+docs-rs
Summary:        Safe libseat bindings - feature "docs_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libseat-sys-0.2/docs-rs) >= 0.2.0
Provides:       crate(%{pkgname}/docs-rs) = %{version}

%description -n %{name}+docs-rs
This metapackage enables feature "docs_rs" for the Rust libseat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Safe libseat bindings - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust libseat crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
