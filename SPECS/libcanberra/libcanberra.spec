# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcanberra
Version:        0.30
Release:        %autorelease
Summary:        Portable Sound Event Library
License:        LGPL-2.1-or-later
URL:            https://0pointer.de/lennart/projects/libcanberra/
VCS:            git:git://git.0pointer.de/libcanberra
#!RemoteAsset:  sha256:c2b671e67e0c288a69fc33dc1b6f1b534d07882c2aceed37004bf48c601afa72
Source0:        https://0pointer.de/lennart/projects/libcanberra/libcanberra-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-pulse
BuildOption(conf):  --enable-alsa
BuildOption(conf):  --enable-null
BuildOption(conf):  --disable-oss
BuildOption(conf):  --with-builtin=dso
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --disable-gtk
BuildOption(conf):  --disable-gtk-doc

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  libtool
BuildRequires:  pulseaudio-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(tdb)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A small and lightweight implementation of the XDG Sound Theme Specification.

%package        gtk3
Summary:        Gtk+ 3.x Bindings for libcanberra
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk3
Gtk+ 3.x bindings for libcanberra.

%package        devel
Summary:        Development Files for libcanberra Client Development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk3 = %{version}-%{release}

%description    devel
Development Files for libcanberra Client Development.

%post
%systemd_post canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service

%preun
%systemd_preun canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service

%postun
%systemd_postun_with_restart canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service

%files
%license LGPL
%doc README
%{_libdir}/libcanberra.so.*
%dir %{_libdir}/libcanberra-%{version}
%{_libdir}/libcanberra-%{version}/*.so
%{_unitdir}/*.service
%{_bindir}/canberra-boot

%files gtk3
%doc %{_datadir}/gtk-doc
%{_libdir}/libcanberra-gtk3.so.*
%{_libdir}/gtk-3.0/modules/*.so
%{_bindir}/canberra-gtk-play
%{_datadir}/gnome/autostart/libcanberra-login-sound.desktop
%{_datadir}/gnome/shutdown/libcanberra-logout-sound.sh
%dir %{_datadir}/gdm/
%dir %{_datadir}/gdm/autostart/
%dir %{_datadir}/gdm/autostart/LoginWindow/
%{_datadir}/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
%dir %{_libdir}/gnome-settings-daemon-3.0/
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules/
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop

%files devel
%{_includedir}/canberra.h
%{_includedir}/canberra-gtk.h
%{_libdir}/libcanberra.so
%{_libdir}/libcanberra-gtk3.so
%{_libdir}/pkgconfig/libcanberra.pc
%{_libdir}/pkgconfig/libcanberra-gtk3.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libcanberra.vapi
%{_datadir}/vala/vapi/libcanberra-gtk.vapi

%changelog
%autochangelog
