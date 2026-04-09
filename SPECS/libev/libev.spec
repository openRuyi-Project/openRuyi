# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libev
Version:        4.33
Release:        %autorelease
Summary:        An event loop library
License:        BSD-2-Clause
URL:            http://software.schmorp.de/pkg/libev.html
# VCS: TODO: Add cvs link here
#!RemoteAsset
Source:         http://dist.schmorp.de/%{name}/Attic/%{name}-%{version}.tar.gz
# Upstream has received patches to add pkg-config support for years but it always ignored them (yes, no answer at all). But since every distribution creates it we just follow.
Source1:        libev.pc
#!RemoteAsset
Source2:        http://dist.schmorp.de/%{name}/Attic/%{name}-%{version}.tar.gz.sig
#!RemoteAsset
Source3:        http://dist.schmorp.de/signing-key.pub
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig

%description
An event loop that is loosely modeled after libevent.

%package        devel
Summary:        Development files for libev
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
An event loop that is loosely modeled after libevent. Features
include child/PID watchers, periodic timers based on wallclock
(absolute) time (in addition to timers using relative timeouts), as
well as epoll/kqueue/event ports/inotify/eventfd/signalfd support,
timer management, time jump detection and correction.

It can be used as a libevent replacement using its emulation API, or
directly embedded into programs. An optional Perl interface is
available.

This package holds the development files for libev.

%package        libevent-devel
Summary:        Compatibility development header with libevent for %{name}.
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
# The event.h file actually conflicts with the one from libevent-devel
Conflicts:      libevent-devel

%description    libevent-devel
This package contains a development header to make libev compatible with
libevent.

%install -a
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/libev.pc

%files
%license LICENSE
%doc README ev.pod Changes
%{_libdir}/libev.so.4
%{_libdir}/libev.so.4.*

%files devel
%{_includedir}/ev++.h
%{_includedir}/ev.h
%{_libdir}/libev.so
%{_mandir}/man3/ev.3*
%{_libdir}/pkgconfig/libev.pc

%files libevent-devel
%{_includedir}/event.h

%changelog
%autochangelog
