# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name notify
%global full_version 8.0.0
%global pkgname notify-8.0

Name:           rust-notify-8.0
Version:        8.0.0
Release:        %autorelease
Summary:        Rust crate "notify"
License:        CC0-1.0
URL:            https://github.com/notify-rs/notify
#!RemoteAsset:  sha256:2fee8403b3d66ac7b26aee6e40a897d85dc5ce26f44da36b8b73e987cc52e943
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.7.0
Requires:       crate(filetime-0.2/default) >= 0.2.24
Requires:       crate(inotify-0.11) >= 0.11.0
Requires:       crate(kqueue-1.0/default) >= 1.0.8
Requires:       crate(libc-0.2/default) >= 0.2.169
Requires:       crate(log-0.4/default) >= 0.4.22
Requires:       crate(mio-1.0/default) >= 1.0.3
Requires:       crate(mio-1.0/os-ext) >= 1.0.3
Requires:       crate(notify-types-2.0/default) >= 2.0.0
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-io) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-windowsprogramming) >= 0.59.0
Provides:       crate(notify) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "notify"

%package     -n %{name}+crossbeam-channel
Summary:        Cross-platform filesystem notification library - feature "crossbeam-channel"
Requires:       crate(%{pkgname})
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/crossbeam-channel)

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fsevent-sys
Summary:        Cross-platform filesystem notification library - feature "fsevent-sys" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(fsevent-sys-4.0/default) >= 4.1.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fsevent-sys)
Provides:       crate(%{pkgname}/macos-fsevent)

%description -n %{name}+fsevent-sys
This metapackage enables feature "fsevent-sys" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "macos_fsevent" features.

%package     -n %{name}+kqueue
Summary:        Cross-platform filesystem notification library - feature "kqueue"
Requires:       crate(%{pkgname})
Requires:       crate(kqueue-1.0/default) >= 1.0.8
Provides:       crate(%{pkgname}/kqueue)

%description -n %{name}+kqueue
This metapackage enables feature "kqueue" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macos-kqueue
Summary:        Cross-platform filesystem notification library - feature "macos_kqueue"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/kqueue)
Requires:       crate(%{pkgname}/mio)
Provides:       crate(%{pkgname}/macos-kqueue)

%description -n %{name}+macos-kqueue
This metapackage enables feature "macos_kqueue" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Cross-platform filesystem notification library - feature "mio"
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.0.3
Requires:       crate(mio-1.0/os-ext) >= 1.0.3
Provides:       crate(%{pkgname}/mio)

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cross-platform filesystem notification library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(notify-types-2.0/serde) >= 2.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialization-compat-6
Summary:        Cross-platform filesystem notification library - feature "serialization-compat-6"
Requires:       crate(%{pkgname})
Requires:       crate(notify-types-2.0/serialization-compat-6) >= 2.0.0
Provides:       crate(%{pkgname}/serialization-compat-6)

%description -n %{name}+serialization-compat-6
This metapackage enables feature "serialization-compat-6" for the Rust notify crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
