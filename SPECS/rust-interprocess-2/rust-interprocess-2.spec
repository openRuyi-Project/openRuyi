# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name interprocess
%global full_version 2.4.5
%global pkgname interprocess-2

Name:           rust-interprocess-2
Version:        2.4.5
Release:        %autorelease
Summary:        Rust crate "interprocess"
License:        0BSD OR Apache-2.0
URL:            https://github.com/kotauskas/interprocess
#!RemoteAsset:  sha256:fe388dd743f24e2e350318bd4bc67b2ab99599c2c63076cd9397293206779186
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(doctest-file-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.137
Requires:       crate(libc-0.2/extra-traits) >= 0.2.137
Requires:       crate(recvmsg-1/default) >= 1.0.0
Requires:       crate(widestring-1/default) >= 1.0.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-security-authorization) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-pipes) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}

%description
Source code for takopackized Rust crate "interprocess"

%package     -n %{name}+futures-core
Summary:        Interprocess communication toolkit - feature "futures-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.28
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%package     -n %{name}+tokio
Summary:        Interprocess communication toolkit - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(tokio-1/default) >= 1.36.0
Requires:       crate(tokio-1/fs) >= 1.36.0
Requires:       crate(tokio-1/io-util) >= 1.36.0
Requires:       crate(tokio-1/macros) >= 1.36.0
Requires:       crate(tokio-1/net) >= 1.36.0
Requires:       crate(tokio-1/rt) >= 1.36.0
Requires:       crate(tokio-1/sync) >= 1.36.0
Requires:       crate(tokio-1/time) >= 1.36.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
