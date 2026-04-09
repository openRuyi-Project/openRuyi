# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           priv_wrapper
Version:        1.0.1
Release:        %autorelease
Summary:        A library to disable resource limits and other privilege dropping
License:        GPL-3.0-or-later
URL:            http://cwrap.org/
VCS:            git:https://git.samba.org/priv_wrapper.git
#!RemoteAsset
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
BuildSystem:    cmake

# Fix cmocka detection for versions 1.1.6 and later
Patch0:         0001-priv_wrapper-fix-cmocka-1.1.6+-support.patch

BuildOption(conf):  -DUNIT_TESTING=ON

BuildRequires:  cmake
BuildRequires:  cmocka-cmake

Recommends:     cmake
Recommends:     pkgconfig

%description
priv_wrapper aims to help running processes which are dropping privileges or
are restricting resources in test environments.
It can disable chroot, prctl, pledge and setrlmit system calls. A disabled call
always succeeds (i.e. returns 0) and does nothing.
The system call pledge exists only on OpenBSD.

To use it, set the following environment variables:

LD_PRELOAD=libpriv_wrapper.so
PRIV_WRAPPER_CHROOT_DISABLE=1

This package does not have a devel package, because this project is for
development/testing.

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libpriv_wrapper.so*
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/priv_wrapper
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config-version.cmake
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config.cmake
%{_libdir}/pkgconfig/priv_wrapper.pc
%{_mandir}/man1/priv_wrapper.1*

%changelog
%autochangelog
