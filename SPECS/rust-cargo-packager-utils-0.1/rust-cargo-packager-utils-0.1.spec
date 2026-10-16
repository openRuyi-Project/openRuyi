# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-packager-utils
%global full_version 0.1.1
%global pkgname cargo-packager-utils-0.1

Name:           rust-cargo-packager-utils-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "cargo-packager-utils"
License:        Apache-2.0 OR MIT
URL:            https://github.com/crabnebula-dev/cargo-packager
#!RemoteAsset:  sha256:b43458dd2ee3cdab3f5b105acd80791383b730380c929018701313d7d299d4e8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ctor-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/process-relaunch-dangerous-allow-symlink-macos) = %{version}

%description
Source code for takopackized Rust crate "cargo-packager-utils"

%package     -n %{name}+clap
Summary:        Utilities for cargo-packager crates - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.5.0
Requires:       crate(clap-4/derive) >= 4.5.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust cargo-packager-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Utilities for cargo-packager crates - feature "schemars" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.0
Requires:       crate(schemars-0.8/derive) >= 0.8.0
Requires:       crate(schemars-0.8/preserve-order) >= 0.8.0
Requires:       crate(schemars-0.8/url) >= 0.8.0
Provides:       crate(%{pkgname}/schema) = %{version}
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust cargo-packager-utils crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "schema" feature.

%package     -n %{name}+serde
Summary:        Utilities for cargo-packager crates - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cargo-packager-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
