# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-raw-sys
%global full_version 0.12.1
%global pkgname linux-raw-sys-0.12

Name:           rust-linux-raw-sys-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "linux-raw-sys"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/linux-raw-sys
#!RemoteAsset:  sha256:32a66949e030da00e8c7d4434b251670a91556f4144941d37452769c25d58a53
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/auxvec) = %{version}
Provides:       crate(%{pkgname}/bootparam) = %{version}
Provides:       crate(%{pkgname}/btrfs) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/elf) = %{version}
Provides:       crate(%{pkgname}/elf-uapi) = %{version}
Provides:       crate(%{pkgname}/errno) = %{version}
Provides:       crate(%{pkgname}/general) = %{version}
Provides:       crate(%{pkgname}/if-arp) = %{version}
Provides:       crate(%{pkgname}/if-ether) = %{version}
Provides:       crate(%{pkgname}/if-packet) = %{version}
Provides:       crate(%{pkgname}/if-tun) = %{version}
Provides:       crate(%{pkgname}/image) = %{version}
Provides:       crate(%{pkgname}/io-uring) = %{version}
Provides:       crate(%{pkgname}/ioctl) = %{version}
Provides:       crate(%{pkgname}/landlock) = %{version}
Provides:       crate(%{pkgname}/loop-device) = %{version}
Provides:       crate(%{pkgname}/mempolicy) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/netlink) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}
Provides:       crate(%{pkgname}/prctl) = %{version}
Provides:       crate(%{pkgname}/ptrace) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/system) = %{version}
Provides:       crate(%{pkgname}/vm-sockets) = %{version}
Provides:       crate(%{pkgname}/xdp) = %{version}

%description
Source code for takopackized Rust crate "linux-raw-sys"

%package     -n %{name}+default
Summary:        Generated bindings for Linux's userspace API - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/errno) = %{version}
Requires:       crate(%{pkgname}/general) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust linux-raw-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Generated bindings for Linux's userspace API - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/no-std) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust linux-raw-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
