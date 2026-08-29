# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossterm
%global full_version 0.29.0
%global pkgname crossterm-0.29

Name:           rust-crossterm-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "crossterm"
License:        MIT
URL:            https://github.com/crossterm-rs/crossterm
#!RemoteAsset:  sha256:d8b9f2e4c67f833b660cdb0a3523065869fb35570177239812ed4c905aeff87b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.9.0
Requires:       crate(document-features-0.2/default) >= 0.2.11
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(rustix-1/stdio) >= 1.0.0
Requires:       crate(rustix-1/termios) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bracketed-paste) = %{version}

%description
Source code for takopackized Rust crate "crossterm"

%package     -n %{name}+default
Summary:        Crossplatform terminal library for manipulating terminals - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bracketed-paste) = %{version}
Requires:       crate(%{pkgname}/derive-more) = %{version}
Requires:       crate(%{pkgname}/events) = %{version}
Requires:       crate(%{pkgname}/windows) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive-more
Summary:        Crossplatform terminal library for manipulating terminals - feature "derive-more"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-more-2/is-variant) >= 2.0.0
Provides:       crate(%{pkgname}/derive-more) = %{version}

%description -n %{name}+derive-more
This metapackage enables feature "derive-more" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+event-stream
Summary:        Crossplatform terminal library for manipulating terminals - feature "event-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/events) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/event-stream) = %{version}

%description -n %{name}+event-stream
This metapackage enables feature "event-stream" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+events
Summary:        Crossplatform terminal library for manipulating terminals - feature "events"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1/default) >= 1.0.0
Requires:       crate(mio-1/os-poll) >= 1.0.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.17
Requires:       crate(signal-hook-mio-0.2/default) >= 0.2.4
Requires:       crate(signal-hook-mio-0.2/support-v1-0) >= 0.2.4
Provides:       crate(%{pkgname}/events) = %{version}

%description -n %{name}+events
This metapackage enables feature "events" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filedescriptor
Summary:        Crossplatform terminal library for manipulating terminals - feature "filedescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(filedescriptor-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/filedescriptor) = %{version}

%description -n %{name}+filedescriptor
This metapackage enables feature "filedescriptor" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Crossplatform terminal library for manipulating terminals - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+osc52
Summary:        Crossplatform terminal library for manipulating terminals - feature "osc52"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/osc52) = %{version}

%description -n %{name}+osc52
This metapackage enables feature "osc52" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Crossplatform terminal library for manipulating terminals - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.9.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-dev-tty
Summary:        Crossplatform terminal library for manipulating terminals - feature "use-dev-tty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/filedescriptor) = %{version}
Requires:       crate(rustix-1/process) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(rustix-1/stdio) >= 1.0.0
Requires:       crate(rustix-1/termios) >= 1.0.0
Provides:       crate(%{pkgname}/use-dev-tty) = %{version}

%description -n %{name}+use-dev-tty
This metapackage enables feature "use-dev-tty" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows
Summary:        Crossplatform terminal library for manipulating terminals - feature "windows"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossterm-winapi-0.9/default) >= 0.9.1
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winerror) >= 0.3.9
Requires:       crate(winapi-0.3/winuser) >= 0.3.9
Provides:       crate(%{pkgname}/windows) = %{version}

%description -n %{name}+windows
This metapackage enables feature "windows" for the Rust crossterm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
