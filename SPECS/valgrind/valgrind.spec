# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _lto_cflags %{nil}
%ifarch riscv64
%global build_cflags -march=rva23u64
%else
%global build_cflags %nil
%endif
%global build_ldflags %nil

%ifarch x86_64
%define valarch amd64
%endif

%ifarch riscv64
%define valarch riscv64
%endif

Name:           valgrind
Version:        3.26.0
Release:        %autorelease
Summary:        Dynamic analysis tools to detect memory or thread bugs
License:        GPL-2.0-or-later
URL:            https://www.valgrind.org/
VCS:            git:https://sourceware.org/git/valgrind.git
#!RemoteAsset
Source0:        https://sourceware.org/pub/valgrind/valgrind-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --enable-only64bit
BuildOption(conf):  --enable-lto=yes
BuildOption(conf):  GDB=%{_bindir}/gdb
BuildOption(conf):  --with-gdbscripts-dir=%{_datadir}/gdb/auto-load
BuildOption(conf):  --without-mpicc

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  automake autoconf
BuildRequires:  perl(Getopt::Long)
BuildRequires:  procps
BuildRequires:  pkgconfig(python3)

%description
Valgrind is an instrumentation framework for building dynamic analysis tools.
There are Valgrind tools that can automatically detect many memory management
and threading bugs, and profile your programs in detail.

%package        devel
Summary:        Development files for valgrind aware programs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for development of valgrind aware programs.

%package        docs
Summary:        Documentation for valgrind tools
License:        GFDL-1.2-or-later

%description    docs
Documentation for valgrind tools and scripts.

%package        gdb
Summary:        Tools for integrating valgrind and gdb
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gdb

%description    gdb
Tools and support files for integrating valgrind and gdb.

%package        tools-devel
Summary:        Development files for building valgrind tools
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    tools-devel
Header files and libraries for development of valgrind tools.

%conf -p
./autogen.sh

%files
%license COPYING
%{_bindir}/valgrind
%{_bindir}/callgrind_*
%{_bindir}/cg_*
%{_bindir}/ms_print
%dir %{_libexecdir}/valgrind
%{_libexecdir}/valgrind/default.supp
%{_libexecdir}/valgrind/*-*-linux
%attr(0755,root,root) %{_libexecdir}/valgrind/vgpreload_*-%{valarch}-linux.so
# Scripts
%{_libexecdir}/valgrind/dh_view.*

%files docs
%license COPYING.DOCS
%doc NEWS README*
%{_datadir}/doc/valgrind/
%{_mandir}/man1/*

%files gdb
%license COPYING
%{_bindir}/valgrind-di-server
%{_bindir}/valgrind-listener
%{_bindir}/vgdb
%{_bindir}/vgstack
%{_libexecdir}/valgrind/*.xml
%{_datadir}/gdb/auto-load/valgrind-monitor*.py

%files devel
%dir %{_includedir}/valgrind
%{_includedir}/valgrind/valgrind.h
%{_includedir}/valgrind/cachegrind.h
%{_includedir}/valgrind/callgrind.h
%{_includedir}/valgrind/drd.h
%{_includedir}/valgrind/helgrind.h
%{_includedir}/valgrind/memcheck.h
%{_includedir}/valgrind/dhat.h
%{_libdir}/pkgconfig/valgrind.pc

%files tools-devel
%license COPYING
%{_includedir}/valgrind/config.h
%{_includedir}/valgrind/libvex*h
%{_includedir}/valgrind/pub_tool_*h
%{_includedir}/valgrind/vki
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*.a

%changelog
%autochangelog
