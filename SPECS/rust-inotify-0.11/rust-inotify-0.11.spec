# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inotify
%global full_version 0.11.1
%global pkgname inotify-0.11

Name:           rust-inotify-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "inotify"
License:        ISC
URL:            https://github.com/hannobraun/inotify
#!RemoteAsset:  sha256:bd5b3eaf1a28b758ac0faa5a4254e8ab2705605496f1b1f3fbbc3988ad73d199
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(inotify-sys-0.1/default) >= 0.1.5
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "inotify"

%package     -n %{name}+futures-core
Summary:        Idiomatic wrapper for inotify - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.30
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Idiomatic wrapper for inotify - feature "stream" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        Idiomatic wrapper for inotify - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.40.0
Requires:       crate(tokio-1/net) >= 1.40.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
