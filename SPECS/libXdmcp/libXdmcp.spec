# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXdmcp
Version:        1.1.5
Release:        %autorelease
Summary:        X Display Manager Control Protocol library
License:        MIT
URL:            http://xorg.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxdmcp.git
#!RemoteAsset
Source:         http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)

%description
The X Display Manager Control Protocol (XDMCP) provides a uniform
mechanism for an autonomous display to request login service from a
remote host. By autonomous, we mean the display consists of hardware
and processes that are independent of any particular host where login
service is desired. An X terminal (screen, keyboard, mouse,
processor, network interface) is a prime example of an autonomous
display.

%package        devel
Summary:        Development files for the XDM Control Protocol library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The X Display Manager Control Protocol (XDMCP) provides a uniform
mechanism for an autonomous display to request login service from a
remote host. By autonomous, we mean the display consists of hardware
and processes that are independent of any particular host where login
service is desired. An X terminal (screen, keyboard, mouse,
processor, network interface) is a prime example of an autonomous
display.

This package contains the development headers for the library found
in %{name}.

%conf -p
autoreconf -fi

%files
%defattr(-,root,root)
%{_libdir}/libXdmcp.so.6*

%files devel
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_docdir}/libXdmcp

%changelog
%autochangelog
