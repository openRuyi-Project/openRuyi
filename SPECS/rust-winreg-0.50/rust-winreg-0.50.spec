# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winreg
%global full_version 0.50.0
%global pkgname winreg-0.50

Name:           rust-winreg-0.50
Version:        0.50.0
Release:        %autorelease
Summary:        Rust crate "winreg"
License:        MIT
URL:            https://github.com/gentoo90/winreg-rs
#!RemoteAsset:  sha256:524e57b2c537c0f9b1e69f1965311ec12182b4122e45035b1508cd24d2adadb1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-security) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-storage-filesystem) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-diagnostics-debug) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-registry) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-time) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/transactions) = %{version}

%description
Source code for takopackized Rust crate "winreg"

%package     -n %{name}+chrono
Summary:        Rust bindings to MS Windows Registry API - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust bindings to MS Windows Registry API - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialization-serde
Summary:        Rust bindings to MS Windows Registry API - feature "serialization-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/transactions) = %{version}
Provides:       crate(%{pkgname}/serialization-serde) = %{version}

%description -n %{name}+serialization-serde
This metapackage enables feature "serialization-serde" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
