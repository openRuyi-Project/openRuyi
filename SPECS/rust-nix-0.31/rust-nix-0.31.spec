# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nix
%global full_version 0.31.3
%global pkgname nix-0.31

Name:           rust-nix-0.31
Version:        0.31.3
Release:        %autorelease
Summary:        Rust crate "nix"
License:        MIT
URL:            https://github.com/nix-rust/nix
#!RemoteAsset:  sha256:cf20d2fde8ff38632c426f1165ed7436270b44f199fc55284c38276f9db47c3d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.3.3
Requires:       crate(cfg-aliases-0.2) >= 0.2.1
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(libc-0.2/extra-traits) >= 0.2.186
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/acct) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dir) = %{version}
Provides:       crate(%{pkgname}/env) = %{version}
Provides:       crate(%{pkgname}/event) = %{version}
Provides:       crate(%{pkgname}/fanotify) = %{version}
Provides:       crate(%{pkgname}/feature) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/hostname) = %{version}
Provides:       crate(%{pkgname}/inotify) = %{version}
Provides:       crate(%{pkgname}/ioctl) = %{version}
Provides:       crate(%{pkgname}/kmod) = %{version}
Provides:       crate(%{pkgname}/mman) = %{version}
Provides:       crate(%{pkgname}/mount) = %{version}
Provides:       crate(%{pkgname}/mqueue) = %{version}
Provides:       crate(%{pkgname}/personality) = %{version}
Provides:       crate(%{pkgname}/poll) = %{version}
Provides:       crate(%{pkgname}/process) = %{version}
Provides:       crate(%{pkgname}/pthread) = %{version}
Provides:       crate(%{pkgname}/ptrace) = %{version}
Provides:       crate(%{pkgname}/quota) = %{version}
Provides:       crate(%{pkgname}/reboot) = %{version}
Provides:       crate(%{pkgname}/resource) = %{version}
Provides:       crate(%{pkgname}/sched) = %{version}
Provides:       crate(%{pkgname}/signal) = %{version}
Provides:       crate(%{pkgname}/syslog) = %{version}
Provides:       crate(%{pkgname}/term) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/ucontext) = %{version}
Provides:       crate(%{pkgname}/uio) = %{version}
Provides:       crate(%{pkgname}/user) = %{version}

%description
Source code for takopackized Rust crate "nix"

%package     -n %{name}+memoffset
Summary:        Rust friendly bindings to *nix APIs - feature "memoffset" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memoffset-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/memoffset) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/socket) = %{version}

%description -n %{name}+memoffset
This metapackage enables feature "memoffset" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "net", and "socket" features.

%package     -n %{name}+pin-utils
Summary:        Rust friendly bindings to *nix APIs - feature "pin-utils" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-utils-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/aio) = %{version}
Provides:       crate(%{pkgname}/pin-utils) = %{version}

%description -n %{name}+pin-utils
This metapackage enables feature "pin-utils" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "aio" feature.

%package     -n %{name}+zerocopy
Summary:        Rust friendly bindings to *nix APIs - feature "zerocopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/uio) = %{version}
Provides:       crate(%{pkgname}/zerocopy) = %{version}

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
