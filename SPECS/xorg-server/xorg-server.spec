# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xorg-server
Version:        21.1.21
Release:        %autorelease
Summary:        The X.org X server
License:        Adobe-Display-PostScript AND BSD-3-Clause AND DEC-3-Clause AND HPND AND HPND-sell-MIT-disclaimer-xserver AND HPND-sell-variant AND ICU AND ISC AND MIT AND MIT-open-group AND NTP AND SGI-B-2.0 AND SMLNJ AND X11 AND X11-distribute-modifications-variant
URL:            https://gitlab.freedesktop.org/xorg/xserver
#!RemoteAsset
Source:         https://www.x.org/releases/individual/xserver/xorg-server-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dxorg=false
BuildOption(conf):  -Dxnest=true
BuildOption(conf):  -Dxvfb=true
BuildOption(conf):  -Dxephyr=true
BuildOption(conf):  -Dglamor=true
BuildOption(conf):  -Dvendor_name=%{_vendor}
BuildOption(conf):  -Dvendor_name_short=%{_vendor_name}
BuildOption(conf):  -Dvendor_web=%{_vendor_url}

BuildRequires:  meson
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dri3proto) >= 1.4
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(inputproto) >= 2.3.99.1
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto) >= 1.4
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-shm) >= 1.9.3
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-xkb)
# For testcases
BuildRequires:  xkeyboard-config
BuildRequires:  xkbcomp

%description
This package should contain the X.org X server, but currently only a stub
package holding some document because openRuyi currently does not need
the modular X server (only X server variants provided by X.org).

%package        xnest
Summary:        Nesting X server
Requires:       xkeyboard-config
Requires:       xkbcomp

%description    xnest
This package contains a nesting X server (a X server running under another).

%package        xephyr
Summary:        Nesting X server with Xrender acceleration
Requires:       xkeyboard-config
Requires:       xkbcomp

%description    xephyr
This package contains a nesting X server, which is different to Xnest because
it utilizes GPU acceleration to implement Xrender (however GPU acceleration
is still not available to clients of this server).

%package        xvfb
Summary:        Headless X server
Requires:       xkeyboard-config
Requires:       xkbcomp

%description    xvfb
This package contains a X server rendering to a virtual framebuffer in the
system memory, which is useful for headless automation processes.

%files
%doc README.md
%license COPYING
%{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt

%files xnest
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files xephyr
%{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*

%files xvfb
%{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%changelog
%autochangelog
