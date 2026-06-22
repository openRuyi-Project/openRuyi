# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name accesskit_unix
%global full_version 0.17.2
%global pkgname accesskit-unix-0.17

Name:           rust-accesskit-unix-0.17
Version:        0.17.2
Release:        %autorelease
Summary:        Rust crate "accesskit_unix"
License:        MIT OR Apache-2.0
URL:            https://github.com/AccessKit/accesskit
#!RemoteAsset:  sha256:301e55b39cfc15d9c48943ce5f572204a551646700d0e8efa424585f94fec528
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(accesskit-0.21/default) >= 0.21.1
Requires:       crate(accesskit-atspi-common-0.14/default) >= 0.14.2
Requires:       crate(atspi-0.25/async-std) >= 0.25.0
Requires:       crate(futures-lite-2/default) >= 2.3.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(zbus-5/async-io) >= 5.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "accesskit_unix"

%package     -n %{name}+async-io
Summary:        AccessKit UI accessibility infrastructure: Linux adapter - feature "async-io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-channel-2/default) >= 2.1.1
Requires:       crate(async-executor-1/default) >= 1.5.0
Requires:       crate(async-task-4/default) >= 4.3.0
Requires:       crate(futures-util-0.3/default) >= 0.3.27
Provides:       crate(%{pkgname}/async-io) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust accesskit_unix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        AccessKit UI accessibility infrastructure: Linux adapter - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.32.0
Requires:       crate(tokio-1/macros) >= 1.32.0
Requires:       crate(tokio-1/net) >= 1.32.0
Requires:       crate(tokio-1/rt) >= 1.32.0
Requires:       crate(tokio-1/sync) >= 1.32.0
Requires:       crate(tokio-1/time) >= 1.32.0
Requires:       crate(tokio-stream-0.1/default) >= 0.1.14
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust accesskit_unix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
