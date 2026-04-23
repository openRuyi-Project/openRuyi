# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           Xwayland
Version:        24.1.10
Release:        %autorelease
Summary:        Xwayland is an X server for running X clients under Wayland.
License:        MIT
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/xserver
#!RemoteAsset:  sha256:459762be8ea046c94386687d77a87add6073868bee14f02913eafebb945b7aa0
Source0:        https://www.x.org/pub/individual/xserver/xwayland-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuilder_string="%{vendor_name} %{name} %{version}-%{release}"
BuildOption(conf):  -Dxkb_output_dir=%{_localstatedir}/lib/xkb
BuildOption(conf):  -Dserverconfigdir=%{_datadir}/xwayland
BuildOption(conf):  -Dxcsecurity=true
BuildOption(conf):  -Dglamor=true
BuildOption(conf):  -Ddri3=true

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(epoxy) >= 1.5.5
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(libdrm) >= 2.4.89
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(xtrans) >= 1.3.2
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(libdecor-0) >= 0.1.1
BuildRequires:  pkgconfig(liboeffis-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libei-1.0) >= 1.0.0
BuildRequires:  xorgproto
BuildRequires:  mesa-gl
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)

Requires:       xkeyboard-config
Requires:       xkbcomp
Recommends:     mesa-gl

%description
Xwayland is an X server for running X clients under Wayland.

%package        devel
Summary:        Development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland.

%install -a
rm %{buildroot}%{_mandir}/man1/Xserver.1*
rm -Rf %{buildroot}%{_includedir}/xorg
rm -Rf %{buildroot}%{_datadir}/aclocal

%check
# skip %check as the building environment does not have monitor
# attached to it

%files
%dir %{_datadir}/xwayland
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*
%{_datadir}/applications/org.freedesktop.Xwayland.desktop

%files devel
%{_libdir}/pkgconfig/xwayland.pc
%{_datadir}/xwayland/protocol.txt

%changelog
%autochangelog
