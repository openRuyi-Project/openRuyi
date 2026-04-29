# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name security-framework
%global full_version 3.7.0
%global pkgname security-framework-3.0

Name:           rust-security-framework-3.0
Version:        3.7.0
Release:        %autorelease
Summary:        Rust crate "security-framework"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/security_framework
#!RemoteAsset:  sha256:b7f4bc775c73d9a02cde8bf7b2ec4c9d12743edf609006c7facc23998404cd1d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(core-foundation-0.10/default) >= 0.10.1
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.7
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(security-framework-sys-2.0) >= 2.17.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/osx-10-12)
Provides:       crate(%{pkgname}/osx-10-13)
Provides:       crate(%{pkgname}/osx-10-14)
Provides:       crate(%{pkgname}/alpn)
Provides:       crate(%{pkgname}/job-bless)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/session-tickets)
Provides:       crate(%{pkgname}/sync-keychain)

%description
Source code for takopackized Rust crate "security-framework"

%package     -n %{name}+osx-10-15
Summary:        Security.framework bindings for macOS and iOS - feature "OSX_10_15"
Requires:       crate(%{pkgname})
Requires:       crate(security-framework-sys-2.0/osx-10-15) >= 2.17.0
Provides:       crate(%{pkgname}/osx-10-15)

%description -n %{name}+osx-10-15
This metapackage enables feature "OSX_10_15" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Security.framework bindings for macOS and iOS - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alpn)
Requires:       crate(%{pkgname}/osx-10-14)
Requires:       crate(%{pkgname}/session-tickets)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Security.framework bindings for macOS and iOS - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.20
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macos-12
Summary:        Security.framework bindings for macOS and iOS - feature "macos-12"
Requires:       crate(%{pkgname})
Requires:       crate(security-framework-sys-2.0/macos-12) >= 2.17.0
Provides:       crate(%{pkgname}/macos-12)

%description -n %{name}+macos-12
This metapackage enables feature "macos-12" for the Rust security-framework crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
