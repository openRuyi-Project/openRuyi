# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libevent
Version:        2.1.12
Release:        %autorelease
Summary:        An event notification library
License:        BSD-3-Clause
URL:            http://libevent.org/
VCS:            git:https://github.com/libevent/libevent
#!RemoteAsset
Source0:        https://github.com/libevent/libevent/releases/download/release-%{version}-stable/libevent-%{version}-stable.tar.gz
#!RemoteAsset
Source1:        https://github.com/libevent/libevent/releases/download/release-%{version}-stable/libevent-%{version}-stable.tar.gz.asc
BuildSystem:    autotools

# PATCH-FEATURE-UPSTREAM 0001-evwatch-Add-prepare-and-check-watchers.patch
Patch0:         0001-evwatch-Add-prepare-and-check-watchers.patch
# PATCH-FEATURE-UPSTREAM 0002-evwatch-fix-race-condition.patch
Patch1:         0002-evwatch-fix-race-condition.patch

BuildOption(conf):  --disable-libevent-regress

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

%package        devel
Summary:        Development files for libevent2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel
# Both have /usr/include/event.h
Conflicts:      libev-libevent-devel
Provides:       %{name}:%{_includedir}/event.h

%description    devel
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

This package holds the development files for libevent2.

%package        static
Summary:        Static libraries for libevent2
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

This package holds the static libraries for libevent2.

%conf -p
./autogen.sh
export ac_cv_func_select=no

%files
%defattr(-,root,root,-)
%license LICENSE
%doc ChangeLog whatsnew-2.0.txt whatsnew-2.1.txt
%{_libdir}/%{name}-*.so.*
%{_libdir}/%{name}_core-*.so.*
%{_libdir}/%{name}_extra-*.so.*
%{_libdir}/%{name}_pthreads-*.so.*
%{_libdir}/%{name}_openssl-*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/event_rpcgen.py
%{_includedir}/evdns.h
%{_includedir}/event.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%{_includedir}/event2
%{_libdir}/%{name}.so
%{_libdir}/%{name}_core.so
%{_libdir}/%{name}_extra.so
%{_libdir}/%{name}_pthreads.so
%{_libdir}/%{name}_openssl.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_pthreads.pc
%{_libdir}/pkgconfig/%{name}_openssl.pc
%{_libdir}/pkgconfig/%{name}_core.pc
%{_libdir}/pkgconfig/%{name}_extra.pc

%files static
%defattr(-,root,root)
%{_libdir}/%{name}.a
%{_libdir}/%{name}_core.a
%{_libdir}/%{name}_extra.a
%{_libdir}/%{name}_openssl.a
%{_libdir}/%{name}_pthreads.a

%changelog
%autochangelog
