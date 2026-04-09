# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ledmon
Version:        1.1.0
Release:        %autorelease
Summary:        Enclosure LED Utilities
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/intel/ledmon
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-systemd=yes
BuildOption(conf):  --enable-library
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  autoconf-archive
BuildRequires:  make
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  libtool
BuildRequires:  pkgconfig(libpci)
BuildRequires:  sg3_utils-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

Provides:       ledctl = %{version}-%{release}
Provides:       %{name}-libs = %{version}-%{release}

Requires:       pciutils
Requires:       sg3_utils-libs

%description
The ledmon and ledctl are user space applications design to control LED
associated with each slot in an enclosure or a drive bay. There are two
types of system: 2-LED system (Activity LED, Status LED) and 3-LED system
(Activity LED, Locate LED, Fail LED). User must have root privileges to
use this application.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libpci)
Requires:       sg3_utils-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%post
%systemd_post ledmon.service

%preun
%systemd_preun ledmon.service

%postun
%systemd_postun_with_restart ledmon.service

%files
%doc README.md COPYING
%{_sbindir}/ledctl
%{_sbindir}/ledmon
%{_mandir}/*/*
%{_unitdir}/ledmon.service
# ledmon libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ledmon.pc

%changelog
%autochangelog
