# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_info
%global full_version 3.14.0
%global pkgname os-info-3.0

Name:           rust-os-info-3.0
Version:        3.14.0
Release:        %autorelease
Summary:        Rust crate "os_info"
License:        MIT
URL:            https://github.com/stanislav-tkach/os_info
#!RemoteAsset:  sha256:e4022a17595a00d6a369236fdae483f0de7f0a339960a53118b818238e132224
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(android-system-properties-0.1/default) >= 0.1.5
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(nix-0.30/default) >= 0.30.1
Requires:       crate(nix-0.30/feature) >= 0.30.1
Requires:       crate(objc2-0.6/default) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/default) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsenumerator) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-ui-kit-0.3/default) >= 0.3.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-registry) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.2
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "os_info"

%package     -n %{name}+schemars
Summary:        Detect the operating system type and version - feature "schemars"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname}/schemars)

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust os_info crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Detect the operating system type and version - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust os_info crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
