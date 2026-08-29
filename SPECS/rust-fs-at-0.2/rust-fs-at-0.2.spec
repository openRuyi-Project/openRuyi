# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fs_at
%global full_version 0.2.1
%global pkgname fs-at-0.2

Name:           rust-fs-at-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "fs_at"
License:        Apache-2.0
URL:            https://github.com/rbtcollins/fs_at.git
#!RemoteAsset:  sha256:14af6c9694ea25db25baa2a1788703b9e7c6648dcaeeebeb98f7561b5384c036
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-0.4/default) >= 0.4.1
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cvt-0.1/default) >= 0.1.1
Requires:       crate(libc-0.2/default) >= 0.2.153
Requires:       crate(nix-0.29/dir) >= 0.29.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/wdk-system-systemservices) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-security) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-ioctl) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-kernel) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-systemservices) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-windowsprogramming) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fs_at"

%package     -n %{name}+log
Summary:        'at' functions for various platforms - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.21
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust fs_at crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+workaround-procmon
Summary:        'at' functions for various platforms - feature "workaround-procmon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.19.0
Provides:       crate(%{pkgname}/workaround-procmon) = %{version}

%description -n %{name}+workaround-procmon
This metapackage enables feature "workaround-procmon" for the Rust fs_at crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
