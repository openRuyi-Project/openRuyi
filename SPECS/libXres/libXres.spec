# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXres
Version:        1.2.2
Release:        %autorelease
Summary:        X-Resource extension client library
License:        X11
URL:            http://www.x.org
# No VCS link
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11) >= 1.5.99.902

%description
X-Resource is an extension that allows a client to query
the X server about its usage of various resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 libXres development package

%install -a
# manually remove static lib
rm %{buildroot}%{_libdir}/*.a

%files
%doc AUTHORS COPYING
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0

%files devel
%{_includedir}/X11/extensions/XRes.h
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_mandir}/man3/*.3*

%changelog
%{?autochangelog}
