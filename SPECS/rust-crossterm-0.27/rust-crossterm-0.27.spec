# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossterm
%global full_version 0.27.0
%global pkgname crossterm-0.27

Name:           rust-crossterm-0.27
Version:        0.27.0
Release:        %autorelease
Summary:        Rust crate "crossterm"
License:        MIT
URL:            https://github.com/crossterm-rs/crossterm
#!RemoteAsset:  sha256:f476fe445d41c9e991fd07515a6f463074b782242ccf4a5b7b1d1012e70824df
Source:         https://static.crates.io/crates/crossterm/0.27.0/download#/rust-crossterm-0.27-0.27.0.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.3.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "crossterm"

%package     -n %{name}+bracketed-paste
Summary:        Crossplatform terminal library for manipulating terminals - feature "bracketed-paste" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bracketed-paste) = %{version}
Provides:       crate(%{pkgname}/windows) = %{version}

%description -n %{name}+bracketed-paste
This metapackage enables feature "bracketed-paste" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "windows" feature.

%package     -n %{name}+default
Summary:        Crossplatform terminal library for manipulating terminals - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bracketed-paste) = %{version}
Requires:       crate(%{pkgname}/events) = %{version}
Requires:       crate(%{pkgname}/windows) = %{version}
Requires:       crate(mio-0.8/default) >= 0.8.0
Requires:       crate(mio-0.8/os-poll) >= 0.8.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.17
Requires:       crate(signal-hook-mio-0.2/default) >= 0.2.3
Requires:       crate(signal-hook-mio-0.2/support-v0-8) >= 0.2.3
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+event-stream
Summary:        Crossplatform terminal library for manipulating terminals - feature "event-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/events) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(mio-0.8/default) >= 0.8.0
Requires:       crate(mio-0.8/os-poll) >= 0.8.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.17
Requires:       crate(signal-hook-mio-0.2/default) >= 0.2.3
Requires:       crate(signal-hook-mio-0.2/support-v0-8) >= 0.2.3
Provides:       crate(%{pkgname}/event-stream) = %{version}

%description -n %{name}+event-stream
This metapackage enables feature "event-stream" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+events
Summary:        Crossplatform terminal library for manipulating terminals - feature "events"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.8/default) >= 0.8.0
Requires:       crate(mio-0.8/os-poll) >= 0.8.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.17
Requires:       crate(signal-hook-mio-0.2/default) >= 0.2.3
Requires:       crate(signal-hook-mio-0.2/support-v0-8) >= 0.2.3
Provides:       crate(%{pkgname}/events) = %{version}

%description -n %{name}+events
This metapackage enables feature "events" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filedescriptor
Summary:        Crossplatform terminal library for manipulating terminals - feature "filedescriptor" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(filedescriptor-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/filedescriptor) = %{version}
Provides:       crate(%{pkgname}/use-dev-tty) = %{version}

%description -n %{name}+filedescriptor
This metapackage enables feature "filedescriptor" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use-dev-tty" feature.

%package     -n %{name}+serde
Summary:        Crossplatform terminal library for manipulating terminals - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/default) >= 2.3.0
Requires:       crate(bitflags-2/serde) >= 2.3.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
