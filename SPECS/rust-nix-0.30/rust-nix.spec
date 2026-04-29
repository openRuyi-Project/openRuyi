# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nix
%global full_version 0.30.1
%global pkgname nix-0.30

Name:           rust-nix-0.30
Version:        0.30.1
Release:        %autorelease
Summary:        Rust crate "nix"
License:        MIT
URL:            https://github.com/nix-rust/nix
#!RemoteAsset:  sha256:74523f3a35e05aba87a1d978330aef40f67b0304ac79c1c00b294c9830543db6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cfg-aliases-0.2/default) >= 0.2.1
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libc-0.2/extra-traits) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/acct)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/dir)
Provides:       crate(%{pkgname}/env)
Provides:       crate(%{pkgname}/event)
Provides:       crate(%{pkgname}/fanotify)
Provides:       crate(%{pkgname}/feature)
Provides:       crate(%{pkgname}/fs)
Provides:       crate(%{pkgname}/hostname)
Provides:       crate(%{pkgname}/inotify)
Provides:       crate(%{pkgname}/ioctl)
Provides:       crate(%{pkgname}/kmod)
Provides:       crate(%{pkgname}/mman)
Provides:       crate(%{pkgname}/mount)
Provides:       crate(%{pkgname}/mqueue)
Provides:       crate(%{pkgname}/personality)
Provides:       crate(%{pkgname}/poll)
Provides:       crate(%{pkgname}/process)
Provides:       crate(%{pkgname}/pthread)
Provides:       crate(%{pkgname}/ptrace)
Provides:       crate(%{pkgname}/quota)
Provides:       crate(%{pkgname}/reboot)
Provides:       crate(%{pkgname}/resource)
Provides:       crate(%{pkgname}/sched)
Provides:       crate(%{pkgname}/signal)
Provides:       crate(%{pkgname}/syslog)
Provides:       crate(%{pkgname}/term)
Provides:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/ucontext)
Provides:       crate(%{pkgname}/uio)
Provides:       crate(%{pkgname}/user)

%description
Source code for takopackized Rust crate "nix"

%package     -n %{name}+memoffset
Summary:        Rust friendly bindings to *nix APIs - feature "memoffset" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(memoffset-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/memoffset)
Provides:       crate(%{pkgname}/net)
Provides:       crate(%{pkgname}/socket)

%description -n %{name}+memoffset
This metapackage enables feature "memoffset" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "net", and "socket" features.

%package     -n %{name}+pin-utils
Summary:        Rust friendly bindings to *nix APIs - feature "pin-utils" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pin-utils-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/aio)
Provides:       crate(%{pkgname}/pin-utils)

%description -n %{name}+pin-utils
This metapackage enables feature "pin-utils" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "aio" feature.

%package     -n %{name}+zerocopy
Summary:        Rust friendly bindings to *nix APIs - feature "zerocopy"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fs)
Requires:       crate(%{pkgname}/uio)
Provides:       crate(%{pkgname}/zerocopy)

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust nix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
