# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inotify
%global full_version 0.11.0
%global pkgname inotify-0.11

Name:           rust-inotify-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "inotify"
License:        ISC
URL:            https://github.com/hannobraun/inotify
#!RemoteAsset:  sha256:f37dccff2791ab604f9babef0ba14fbe0be30bd368dc541e2b08d07c8aa908f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.7.0
Requires:       crate(inotify-sys-0.1/default) >= 0.1.5
Requires:       crate(libc-0.2/default) >= 0.2.169
Provides:       crate(inotify) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "inotify"

%package     -n %{name}+futures-core
Summary:        Idiomatic wrapper for inotify - feature "futures-core"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/futures-core)

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Idiomatic wrapper for inotify - feature "stream" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/stream)

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        Idiomatic wrapper for inotify - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.0.1
Requires:       crate(tokio-1.0/net) >= 1.0.1
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust inotify crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
