# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global libname xcb-xrm

Name:           xcb-util-xrm
Version:        1.3
Release:        %autorelease
Summary:        XCB utility functions for the X resource manager
License:        MIT
URL:            https://github.com/Airblader/xcb-util-xrm
VCS:            git:https://github.com/Airblader/xcb-util-xrm.git
#!RemoteAsset:  sha256:0129f74c327ae65e2f4ad4002f300b4f02c9aff78c00997f1f1c5a430f922f34
Source0:        https://github.com/Airblader/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xorg-macros)

%description
XCB utility functions for loading and querying X resource manager data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers and library links for developing applications
that use xcb-util-xrm.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_libdir}/lib%{libname}.la

%files
%doc ChangeLog README
%license COPYING
%{_libdir}/lib%{libname}.so.*

%files devel
%license COPYING
%{_includedir}/xcb/xcb_xrm.h
%{_libdir}/lib%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
%autochangelog
