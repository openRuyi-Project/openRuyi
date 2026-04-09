# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define sonum 1
%define libname libproc2

Name:          procps-ng
Version:       4.0.5
Release:       %autorelease
Summary:       System and process monitoring utilities
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
URL:           https://gitlab.com/procps-ng/procps
#!RemoteAsset
Source0:       https://downloads.sourceforge.net/project/%{name}/Production/%{name}-%{version}.tar.xz
BuildSystem:   autotools

BuildOption(conf):  --disable-kill
BuildOption(conf):  --enable-watch8bit
BuildOption(conf):  --with-systemd
BuildOption(conf):  --sbindir=%{_bindir}
BuildOption(check):  LD_LIBRARY_PATH=$PWD/proc/.libs

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libsystemd)

Provides:       procps

%description
The procps-ng package contains a set of system utilities that provide
system information, such as ps, top, free, vmstat, and watch.

%package        devel
Summary:        Development files for procps-ng
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries for procps-ng.

%conf -p
# Use autoreconf to regenerate build files, this is more robust than ./autogen.sh
autoreconf -fiv

%install -a
# Cleanup unnecessary files.
# kill and uptime are provided by other core packages (util-linux).
rm -f %{buildroot}%{_bindir}/kill
rm -f %{buildroot}%{_bindir}/uptime
rm -f %{buildroot}%{_mandir}/man1/kill.1*
rm -f %{buildroot}%{_mandir}/man1/uptime.1*
rm -rf %{buildroot}%{_mandir}/pl/man5
rm -rf %{buildroot}%{_mandir}/{fr,de,pt_BR}/man3

# Package localization files using the find_lang macro for the -lang subpackage.
%find_lang %{name}  --all-name --with-man --generate-subpackages

%files
%license COPYING COPYING.LIB
%doc doc/bugs.md doc/FAQ NEWS README.md doc/libproc.supp
%{_libdir}/%{libname}.so.%{sonum}*
%{_bindir}/free
%{_bindir}/hugetop
%{_bindir}/pgrep
%{_bindir}/pkill
%{_bindir}/pidof
%{_bindir}/pidwait
%{_bindir}/pmap
%{_bindir}/ps
%{_bindir}/pwdx
%{_bindir}/slabtop
%{_bindir}/sysctl
%{_bindir}/tload
%{_bindir}/top
%{_bindir}/w
%{_bindir}/watch
%{_bindir}/vmstat
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%dir %{_includedir}/%{libname}
%{_includedir}/%{libname}/*.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/%{libname}.a
%{_mandir}/man3/*

%changelog
%autochangelog
