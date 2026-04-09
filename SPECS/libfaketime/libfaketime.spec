# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _lto_cflags %{nil}
%global _test_target test

Name:           libfaketime
Version:        0.9.12
Release:        %autorelease
Summary:        FakeTime Preload Library
License:        GPL-2.0-only
URL:            https://github.com/wolfcw/libfaketime
#!RemoteAsset
Source:         https://github.com/wolfcw/libfaketime/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  LIBDIRNAME=%{_libdir}/%{name}
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBDIRNAME=/%{_lib}
%ifarch riscv64
BuildOption(build):  FAKETIME_COMPILE_CFLAGS='%{build_cflags} -DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER'
BuildOption(check):  FAKETIME_COMPILE_CFLAGS='%{build_cflags} -DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER'
%else
BuildOption(build):  FAKETIME_COMPILE_CFLAGS='%{build_cflags}'
BuildOption(check):  FAKETIME_COMPILE_CFLAGS='%{build_cflags}'
%endif

%description
libfaketime allows you to report a faked system time to programs without
having to change the system-wide time, using a preload library.

# No configure
%conf

%files
%doc NEWS README
%license COPYING
%{_bindir}/faketime
%{_mandir}/man1/faketime.1*
%doc %{_docdir}/faketime
%{_libdir}/lib*.so*

%changelog
%autochangelog
