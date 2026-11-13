# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define cross_target riscv64-openruyi-linux
%define cross_sysroot %{_prefix}/%{cross_target}/sys-root

Name:           cross-riscv64-linux-headers
Summary:        Linux headers for %{cross_target} cross-compilation (sysroot)
License:        GPL-2.0-only WITH Linux-syscall-note
Version:        6.18.32
Release:        %autorelease
URL:            https://www.kernel.org/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
#!RemoteAsset:  sha256:067dadd445578284ea6158f312f7970d8940fed3e094dbe49cff66d188d3bda4
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

ExclusiveArch:  x86_64

BuildRequires:  rsync

%description
Linux kernel UAPI headers installed into the cross sysroot at
%{cross_sysroot}, for use when building a riscv64 cross libc/toolchain.

%prep
%autosetup -p1 -n linux-%{version}

%install
%make_build ARCH=riscv headers_install \
    INSTALL_HDR_PATH=%{buildroot}%{cross_sysroot}/usr

%files
%defattr(-,root,root)
%license COPYING
%{cross_sysroot}/usr/include/

%changelog
%autochangelog
