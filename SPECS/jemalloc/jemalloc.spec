# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jemalloc
Version:        5.3.1
Release:        %autorelease
Summary:        general purpose malloc(3) implementation
License:        BSD-2-Clause
URL:            https://jemalloc.net/
VCS:            git:https://github.com/jemalloc/jemalloc
#!RemoteAsset:  sha256:3826bc80232f22ed5c4662f3034f799ca316e819103bdc7bb99018a421706f92
Source0:        https://github.com/jemalloc/jemalloc/releases/download/5.3.1/jemalloc-5.3.1.tar.bz2
BuildSystem:    autotools

# Patch0001 is partially picked from https://github.com/jemalloc/jemalloc/pull/2900
# Note: this patch is already included in jemalloc's dev branch
# Should be dropped in further releases of jemalloc
Patch0:         0001-fix-builds-with-gcc-16.patch
# Use Zihintpause for CPU_SPINWAIT
Patch2000:      2000-fix-riscv-build-without-zihintpause.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static libraries for developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc README VERSION
%doc %{_docdir}/jemalloc/jemalloc.html
%license COPYING
%{_bindir}/jemalloc.sh
%{_bindir}/jeprof
%{_libdir}/libjemalloc.so
%{_libdir}/libjemalloc.so.2

%files devel
%{_bindir}/jemalloc-config
%{_includedir}/jemalloc/jemalloc.h
%{_libdir}/pkgconfig/jemalloc.pc
%{_mandir}/man3/jemalloc.3*

%files static
%{_libdir}/libjemalloc.a
%{_libdir}/libjemalloc_pic.a

%changelog
%autochangelog
