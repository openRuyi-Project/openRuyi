# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mio
%global full_version 1.2.0
%global pkgname mio-1.0

Name:           rust-mio-1.0
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "mio"
License:        MIT
URL:            https://github.com/tokio-rs/mio
#!RemoteAsset:  sha256:50b7e5b27aa02a74bac8c3f23f448f8d87ff11f92d3aac1a6ed369ee08cc56c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(wasi-0.11/default) >= 0.11.1
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/net)
Provides:       crate(%{pkgname}/os-poll)

%description
Source code for takopackized Rust crate "mio"

%package     -n %{name}+log
Summary:        Lightweight non-blocking I/O - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+os-ext
Summary:        Lightweight non-blocking I/O - feature "os-ext"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/os-poll)
Requires:       crate(windows-sys-0.61/wdk-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-pipes) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.2
Provides:       crate(%{pkgname}/os-ext)

%description -n %{name}+os-ext
This metapackage enables feature "os-ext" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
