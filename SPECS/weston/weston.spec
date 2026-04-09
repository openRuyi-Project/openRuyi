# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global apiver 14

%bcond rdp 0
%bcond vnc 0
%bcond pipewire 0
%bcond demo 1
%bcond tests 0

Name:           weston
Version:        14.0.2
Release:        %autorelease
Summary:        Reference compositor for Wayland
License:        MIT and CC-BY-SA-3.0
URL:            http://wayland.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/wayland/weston/
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/wayland/weston/-/releases/%{version}/downloads/weston-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbackend-drm=true
BuildOption(conf):  -Dbackend-drm-screencast-vaapi=true
BuildOption(conf):  -Dbackend-headless=true
BuildOption(conf):  -Dbackend-wayland=true
BuildOption(conf):  -Dxwayland=false
BuildOption(conf):  -Dbackend-x11=true
BuildOption(conf):  -Dremoting=false
BuildOption(conf):  -Dtest-junit-xml=false
BuildOption(conf):  -Dbackend-pipewire=false
%if %{with rdp}
BuildOption(conf):  -Dbackend-rdp=true
%else
BuildOption(conf):  -Dbackend-rdp=false
%endif
%if %{with vnc}
BuildOption(conf):  -Dbackend-vnc=true
%else
BuildOption(conf):  -Dbackend-vnc=false
%endif
%if %{with pipewire}
BuildOption(conf):  -Dpipewire=true
%else
BuildOption(conf):  -Dpipewire=false
%endif
%if %{with demo}
BuildOption(conf):  -Ddemo-clients=true
BuildOption(conf):  -Dsimple-clients=all
%else
BuildOption(conf):  -Ddemo-clients=false
BuildOption(conf):  -Dsimple-clients=
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 10.2
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 0.8.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.25.2
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client) >= 1.22.0
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.33
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(libva) >= 0.34.0
BuildRequires:  pkgconfig(libva-drm) >= 0.34.0
%if %{with rdp}
BuildRequires:  pkgconfig(freerdp3)
%endif
%if %{with vnc}
BuildRequires:  pkgconfig(neatvnc) >= 0.7.0
%endif
%if %{with pipewire}
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
%endif

# The keyboard layout information provided by this package is needed at runtime
Requires:       xkeyboard-config

%description
Weston is the reference wayland compositor that can run on KMS, under X11
or under another compositor.

%package        devel
Summary:        Common headers for weston
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Common headers for weston.

%if %{with demo}
%package        demo
Summary:        Weston demo program files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    demo
This package contains Weston demo program files.
%endif

%check
%if %{with tests}
%meson_test
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/weston
%{_bindir}/weston-debug
%{_bindir}/weston-screenshooter
%{_bindir}/weston-tablet
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/fullscreen-shell.so
%{_libdir}/weston/hmi-controller.so
%{_libdir}/weston/ivi-shell.so
%{_libdir}/weston/kiosk-shell.so
%{_libdir}/weston/screen-share.so
%{_libdir}/weston/systemd-notify.so
%{_libdir}/weston/libexec_weston.so*
%{_libexecdir}/weston-*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg
%{_datadir}/wayland-sessions/weston.desktop
%dir %{_libdir}/libweston-%{apiver}
%{_libdir}/libweston-%{apiver}/color-lcms.so
%{_libdir}/libweston-%{apiver}/drm-backend.so
%{_libdir}/libweston-%{apiver}/gl-renderer.so
%{_libdir}/libweston-%{apiver}/headless-backend.so
%{_libdir}/libweston-%{apiver}/wayland-backend.so
%{_libdir}/libweston-%{apiver}/x11-backend.so
%if %{with rdp}
%{_libdir}/libweston-%{apiver}/rdp-backend.so
%endif
%if %{with vnc}
%{_libdir}/libweston-%{apiver}/vnc-backend.so
%endif
%if %{with pipewire}
%{_libdir}/libweston-%{apiver}/pipewire-backend.so
%{_libdir}/libweston-%{apiver}/pipewire-plugin.so
%endif
%{_libdir}/libweston-%{apiver}.so.0*

%if %{with demo}
%files demo
%{_bindir}/weston-*
%exclude %{_bindir}/weston
%exclude %{_bindir}/weston-debug
%exclude %{_bindir}/weston-screenshooter
%exclude %{_bindir}/weston-tablet
%exclude %{_bindir}/weston-terminal
%endif

%files devel
%{_includedir}/libweston-%{apiver}/
%{_includedir}/weston/
%{_libdir}/pkgconfig/libweston-%{apiver}.pc
%{_libdir}/pkgconfig/weston.pc
%{_libdir}/libweston-%{apiver}.so
%{_datadir}/pkgconfig/libweston-%{apiver}-protocols.pc
%{_datadir}/libweston-%{apiver}/protocols/

%changelog
%autochangelog
