# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name notify
%global full_version 8.2.0
%global pkgname notify-8

Name:           rust-notify-8
Version:        8.2.0
Release:        %autorelease
Summary:        Rust crate "notify"
License:        CC0-1.0
URL:            https://github.com/notify-rs/notify
#!RemoteAsset:  sha256:4d3d07927151ff8575b7087f245456e549fea62edf0ec4e565a5ee50c8402bc3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.7.0
Requires:       crate(inotify-0.11) >= 0.11.0
Requires:       crate(kqueue-1/default) >= 1.1.1
Requires:       crate(libc-0.2/default) >= 0.2.4
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(mio-1/default) >= 1.0.0
Requires:       crate(mio-1/os-ext) >= 1.0.0
Requires:       crate(notify-types-2/default) >= 2.0.0
Requires:       crate(walkdir-2/default) >= 2.4.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.1
Requires:       crate(windows-sys-0.60/win32-system-windowsprogramming) >= 0.60.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "notify"

%package     -n %{name}+crossbeam-channel
Summary:        Cross-platform filesystem notification library - feature "crossbeam-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flume
Summary:        Cross-platform filesystem notification library - feature "flume"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flume-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/flume) = %{version}

%description -n %{name}+flume
This metapackage enables feature "flume" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fsevent-sys
Summary:        Cross-platform filesystem notification library - feature "fsevent-sys" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fsevent-sys-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fsevent-sys) = %{version}
Provides:       crate(%{pkgname}/macos-fsevent) = %{version}

%description -n %{name}+fsevent-sys
This metapackage enables feature "fsevent-sys" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "macos_fsevent" features.

%package     -n %{name}+kqueue
Summary:        Cross-platform filesystem notification library - feature "kqueue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kqueue-1/default) >= 1.1.1
Provides:       crate(%{pkgname}/kqueue) = %{version}

%description -n %{name}+kqueue
This metapackage enables feature "kqueue" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macos-kqueue
Summary:        Cross-platform filesystem notification library - feature "macos_kqueue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kqueue) = %{version}
Requires:       crate(%{pkgname}/mio) = %{version}
Provides:       crate(%{pkgname}/macos-kqueue) = %{version}

%description -n %{name}+macos-kqueue
This metapackage enables feature "macos_kqueue" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Cross-platform filesystem notification library - feature "mio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1/default) >= 1.0.0
Requires:       crate(mio-1/os-ext) >= 1.0.0
Provides:       crate(%{pkgname}/mio) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cross-platform filesystem notification library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(notify-types-2/serde) >= 2.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialization-compat-6
Summary:        Cross-platform filesystem notification library - feature "serialization-compat-6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(notify-types-2/serialization-compat-6) >= 2.0.0
Provides:       crate(%{pkgname}/serialization-compat-6) = %{version}

%description -n %{name}+serialization-compat-6
This metapackage enables feature "serialization-compat-6" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
