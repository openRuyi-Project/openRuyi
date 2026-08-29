# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name security-framework
%global full_version 3.7.0
%global pkgname security-framework-3

Name:           rust-security-framework-3
Version:        3.7.0
Release:        %autorelease
Summary:        Rust crate "security-framework"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/security_framework
#!RemoteAsset:  sha256:b7f4bc775c73d9a02cde8bf7b2ec4c9d12743edf609006c7facc23998404cd1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.11.0
Requires:       crate(core-foundation-0.10/default) >= 0.10.0
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.6
Requires:       crate(libc-0.2/default) >= 0.2.139
Requires:       crate(security-framework-sys-2) >= 2.17.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alpn) = %{version}
Provides:       crate(%{pkgname}/job-bless) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/osx-10-12) = %{version}
Provides:       crate(%{pkgname}/osx-10-13) = %{version}
Provides:       crate(%{pkgname}/osx-10-14) = %{version}
Provides:       crate(%{pkgname}/session-tickets) = %{version}
Provides:       crate(%{pkgname}/sync-keychain) = %{version}

%description
Source code for takopackized Rust crate "security-framework"

%package     -n %{name}+osx-10-15
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(security-framework-sys-2/osx-10-15) >= 2.17.0
Provides:       crate(%{pkgname}/osx-10-15) = %{version}

%description -n %{name}+osx-10-15
This metapackage enables feature "OSX_10_15" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Security.framework bindings for macOS and iOS - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alpn) = %{version}
Requires:       crate(%{pkgname}/osx-10-14) = %{version}
Requires:       crate(%{pkgname}/session-tickets) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Security.framework bindings for macOS and iOS - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.20
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macos-12
Summary:        Security.framework bindings for macOS and iOS - feature "macos-12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(security-framework-sys-2/macos-12) >= 2.17.0
Provides:       crate(%{pkgname}/macos-12) = %{version}

%description -n %{name}+macos-12
This metapackage enables feature "macos-12" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
