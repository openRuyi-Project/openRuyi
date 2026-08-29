# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-foundation
%global full_version 0.9.4
%global pkgname core-foundation-0.9

Name:           rust-core-foundation-0.9
Version:        0.9.4
Release:        %autorelease
Summary:        Rust crate "core-foundation"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/core-foundation-rs
#!RemoteAsset:  sha256:91e195e091a93c46f7102ec7818a2aa394e1e1771c3ab4825963fa03e45afb8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-sys-0.8) >= 0.8.6
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "core-foundation"

%package     -n %{name}+chrono
Summary:        Bindings to Core Foundation for macOS - feature "chrono" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}
Provides:       crate(%{pkgname}/with-chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-chrono" feature.

%package     -n %{name}+link
Summary:        Bindings to Core Foundation for macOS - feature "link" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-foundation-sys-0.8/link) >= 0.8.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/link) = %{version}

%description -n %{name}+link
This metapackage enables feature "link" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+mac-os-10-7-support
Summary:        Bindings to Core Foundation for macOS - feature "mac_os_10_7_support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-foundation-sys-0.8/mac-os-10-7-support) >= 0.8.6
Provides:       crate(%{pkgname}/mac-os-10-7-support) = %{version}

%description -n %{name}+mac-os-10-7-support
This metapackage enables feature "mac_os_10_7_support" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-os-10-8-features
Summary:        Bindings to Core Foundation for macOS - feature "mac_os_10_8_features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-foundation-sys-0.8/mac-os-10-8-features) >= 0.8.6
Provides:       crate(%{pkgname}/mac-os-10-8-features) = %{version}

%description -n %{name}+mac-os-10-8-features
This metapackage enables feature "mac_os_10_8_features" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Bindings to Core Foundation for macOS - feature "uuid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/with-uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-uuid" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
