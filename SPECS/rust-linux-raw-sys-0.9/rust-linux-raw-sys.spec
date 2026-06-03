# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-raw-sys
%global full_version 0.9.4
%global pkgname linux-raw-sys-0.9

Name:           rust-linux-raw-sys-0.9
Version:        0.9.4
Release:        %autorelease
Summary:        Rust crate "linux-raw-sys"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/linux-raw-sys
#!RemoteAsset:  sha256:cd945864f07fe9f5371a27ad7b52a172b4b499999f1d97574c9fa68373937e12
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bootparam)
Provides:       crate(%{pkgname}/btrfs)
Provides:       crate(%{pkgname}/elf)
Provides:       crate(%{pkgname}/elf-uapi)
Provides:       crate(%{pkgname}/errno)
Provides:       crate(%{pkgname}/general)
Provides:       crate(%{pkgname}/if-arp)
Provides:       crate(%{pkgname}/if-ether)
Provides:       crate(%{pkgname}/if-packet)
Provides:       crate(%{pkgname}/image)
Provides:       crate(%{pkgname}/io-uring)
Provides:       crate(%{pkgname}/ioctl)
Provides:       crate(%{pkgname}/landlock)
Provides:       crate(%{pkgname}/loop-device)
Provides:       crate(%{pkgname}/mempolicy)
Provides:       crate(%{pkgname}/net)
Provides:       crate(%{pkgname}/netlink)
Provides:       crate(%{pkgname}/no-std)
Provides:       crate(%{pkgname}/prctl)
Provides:       crate(%{pkgname}/ptrace)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/system)
Provides:       crate(%{pkgname}/xdp)

%description
Source code for takopackized Rust crate "linux-raw-sys"

%package     -n %{name}+default
Summary:        Generated bindings for Linux's userspace API - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/errno)
Requires:       crate(%{pkgname}/general)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust linux-raw-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
