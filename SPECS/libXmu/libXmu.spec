# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXmu
Version:        1.2.1
Release:        %autorelease
Summary:        X.Org X11 libXmu/libXmuu runtime libraries
License:        MIT-open-group AND SMLNJ AND X11 AND ISC
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxmu
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/xorg/lib/libxmu/-/archive/libXmu-%{version}/libxmu-libXmu-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)

%description
X.Org X11 libXmu/libXmuu runtime libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
X.Org X11 libXmu development package.

%conf -p
autoreconf -fiv

%files
%doc COPYING README.md
%{_libdir}/libXmu.so.6*
%{_libdir}/libXmuu.so.1*

%files devel
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/*.h
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/pkgconfig/xmu.pc
%{_libdir}/pkgconfig/xmuu.pc
%doc %{_docdir}/libXmu

%changelog
%autochangelog
