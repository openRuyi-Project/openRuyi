# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name trash
%global full_version 5.2.6
%global pkgname trash-5

Name:           rust-trash-5
Version:        5.2.6
Release:        %autorelease
Summary:        Rust crate "trash"
License:        MIT
URL:            https://github.com/ArturKovacs/trash
#!RemoteAsset:  sha256:7602e0c7d66ec2d92a8c917219fbc7894039efa2063b9064260110828a356f46
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.149
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(objc2-0.6/default) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilemanager) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/std) >= 0.3.2
Requires:       crate(once-cell-1/default) >= 1.7.2
Requires:       crate(percent-encoding-2/default) >= 2.3.1
Requires:       crate(scopeguard-1/default) >= 1.2.0
Requires:       crate(urlencoding-2/default) >= 2.1.3
Requires:       crate(windows-0.56/default) >= 0.56.0
Requires:       crate(windows-0.56/win32-foundation) >= 0.56.0
Requires:       crate(windows-0.56/win32-storage-enhancedstorage) >= 0.56.0
Requires:       crate(windows-0.56/win32-system-com-structuredstorage) >= 0.56.0
Requires:       crate(windows-0.56/win32-system-systemservices) >= 0.56.0
Requires:       crate(windows-0.56/win32-ui-shell-propertiessystem) >= 0.56.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/coinit-apartmentthreaded) = %{version}
Provides:       crate(%{pkgname}/coinit-disable-ole1dde) = %{version}
Provides:       crate(%{pkgname}/coinit-multithreaded) = %{version}
Provides:       crate(%{pkgname}/coinit-speed-over-memory) = %{version}

%description
Source code for takopackized Rust crate "trash"

%package     -n %{name}+chrono
Summary:        Moving files and folders to the Recycle Bin - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.31
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust trash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Moving files and folders to the Recycle Bin - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/coinit-apartmentthreaded) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust trash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
