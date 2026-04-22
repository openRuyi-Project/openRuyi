# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mio
%global full_version 1.0.3
%global pkgname mio-1.0

Name:           rust-mio-1.0
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "mio"
License:        MIT
URL:            https://github.com/tokio-rs/mio
#!RemoteAsset:  sha256:2886843bf800fba2e3377cff24abf6379b4c4d5c6681eaf9ea5b0d15090450bd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.169
Requires:       crate(wasi-0.11/default) >= 0.11.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-windowsprogramming) >= 0.52.0
Provides:       crate(mio) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/net)
Provides:       crate(%{pkgname}/os-poll)

%description
Source code for takopackized Rust crate "mio"

%package     -n %{name}+log
Summary:        Lightweight non-blocking I/O - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.22
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+os-ext
Summary:        Lightweight non-blocking I/O - feature "os-ext"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/os-poll)
Requires:       crate(windows-sys-0.52/wdk-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-security) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-pipes) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-windowsprogramming) >= 0.52.0
Provides:       crate(%{pkgname}/os-ext)

%description -n %{name}+os-ext
This metapackage enables feature "os-ext" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
