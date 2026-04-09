# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXcursor
Version:        1.2.3
Release:        %autorelease
Summary:        Cursor management library
License:        HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/lib/libxcursor
#!RemoteAsset
Source0:        http://xorg.freedesktop.org/archive/individual/lib/libXcursor-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)

%description
This is a simple library designed to help locate and load cursors.
Cursors can be loaded from files or memory.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libXcursor development package.

%prep -a
iconv --from=ISO-8859-2 --to=UTF-8 COPYING > COPYING.new && \
touch -r COPYING COPYING.new && \
mv COPYING.new COPYING

%conf -p
autoreconf -fiv

%install -a
install -d -m 755 %{buildroot}%{_datadir}/icons/default

%files
%doc AUTHORS COPYING README.md
%{_libdir}/libXcursor.so.1*
%dir %{_datadir}/icons/default

%files devel
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/Xcursor.h
%{_libdir}/libXcursor.so
%{_libdir}/pkgconfig/xcursor.pc
%{_mandir}/man3/Xcursor*.3*

%changelog
%autochangelog
