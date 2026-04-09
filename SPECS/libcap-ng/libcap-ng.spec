# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcap-ng
Version:        0.8.5
Release:        %autorelease
Summary:        An alternate Linux/POSIX capabilities library
License:        LGPL-2.1-or-later
URL:            https://people.redhat.com/sgrubb/libcap-ng
VCS:            git:https://github.com/stevegrubb/libcap-ng
#!RemoteAsset
Source:         https://people.redhat.com/sgrubb/%{name}/%{name}-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-python

BuildRequires:  linux-headers
BuildRequires:  pkgconfig

%description
libcap-ng is a library providing an alternate mechanism to libcap to
make use of Linux process and file capabilities. It also contains utilities
for analysing and setting file capabilities.

%package        devel
Summary:        Header files for the libcap-ng library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The libcap-ng-devel package contains the files needed for developing
applications that need to use the libcap-ng library.

%package        utils
Summary:        Utilities for analysing and setting file capabilities
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The libcap-ng-utils package contains applications to analyse the
Linux process capabilities of programs running on a system. It also
lets you set the filesystem-based capabilities.

%conf -p
export LDFLAGS="$LDFLAGS -lpthread"

%files
%license COPYING.LIB
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*
%{_libdir}/libdrop_ambient.so.0
%{_libdir}/libdrop_ambient.so.0.*

%files devel
%{_mandir}/man3/*.3%{ext_man}
%{_mandir}/man7/libdrop_ambient.7%{ext_man}
%{_includedir}/cap-ng.h
%{_libdir}/%{name}.so
%{_libdir}/libdrop_ambient.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/cap-ng.m4
%{_libdir}/pkgconfig/%{name}.pc

%files utils
%license COPYING
%{_bindir}/captest
%{_bindir}/filecap
%{_bindir}/netcap
%{_bindir}/pscap
%{_mandir}/man8/*.8%{ext_man}

%changelog
%autochangelog
