# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossterm
%global full_version 0.28.1
%global pkgname crossterm-0.28

Name:           rust-crossterm-0.28
Version:        0.28.1
Release:        %autorelease
Summary:        Rust crate "crossterm"
License:        MIT
URL:            https://github.com/crossterm-rs/crossterm
#!RemoteAsset:  sha256:829d955a0bb380ef178a640b91779e3987da38c9aea133b20614cfed8cdea9c6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(rustix-0.38/std) >= 0.38.44
Requires:       crate(rustix-0.38/stdio) >= 0.38.44
Requires:       crate(rustix-0.38/termios) >= 0.38.44
Provides:       crate(crossterm) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bracketed-paste)

%description
Source code for takopackized Rust crate "crossterm"

%package     -n %{name}+default
Summary:        Crossplatform terminal library for manipulating terminals - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bracketed-paste)
Requires:       crate(%{pkgname}/events)
Requires:       crate(%{pkgname}/windows)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+event-stream
Summary:        Crossplatform terminal library for manipulating terminals - feature "event-stream"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/events)
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/event-stream)

%description -n %{name}+event-stream
This metapackage enables feature "event-stream" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+events
Summary:        Crossplatform terminal library for manipulating terminals - feature "events"
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.2.0
Requires:       crate(mio-1.0/os-poll) >= 1.2.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.18
Requires:       crate(signal-hook-mio-0.2/default) >= 0.2.5
Requires:       crate(signal-hook-mio-0.2/support-v1-0) >= 0.2.5
Provides:       crate(%{pkgname}/events)

%description -n %{name}+events
This metapackage enables feature "events" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filedescriptor
Summary:        Crossplatform terminal library for manipulating terminals - feature "filedescriptor"
Requires:       crate(%{pkgname})
Requires:       crate(filedescriptor-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/filedescriptor)

%description -n %{name}+filedescriptor
This metapackage enables feature "filedescriptor" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Crossplatform terminal library for manipulating terminals - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Crossplatform terminal library for manipulating terminals - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/serde) >= 2.11.1
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-dev-tty
Summary:        Crossplatform terminal library for manipulating terminals - feature "use-dev-tty"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/filedescriptor)
Requires:       crate(rustix-0.38/process) >= 0.38.44
Requires:       crate(rustix-0.38/std) >= 0.38.44
Requires:       crate(rustix-0.38/stdio) >= 0.38.44
Requires:       crate(rustix-0.38/termios) >= 0.38.44
Provides:       crate(%{pkgname}/use-dev-tty)

%description -n %{name}+use-dev-tty
This metapackage enables feature "use-dev-tty" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows
Summary:        Crossplatform terminal library for manipulating terminals - feature "windows"
Requires:       crate(%{pkgname})
Requires:       crate(crossterm-winapi-0.9/default) >= 0.9.1
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winerror) >= 0.3.9
Requires:       crate(winapi-0.3/winuser) >= 0.3.9
Provides:       crate(%{pkgname}/windows)

%description -n %{name}+windows
This metapackage enables feature "windows" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
