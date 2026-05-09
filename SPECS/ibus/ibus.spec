# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ibus
Version:        1.5.33
Release:        %autorelease
Summary:        Intelligent Input Bus for Linux OS
License:        LGPL-2.1-or-later
URL:            https://github.com/ibus/ibus
#!RemoteAsset:  sha256:58941c9b8285891c776b67fb2039eebe0d61d63a51578519febfc5481b91e831
Source:         https://github.com/ibus/ibus/releases/download/%{version}/ibus-%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/ibus/ibus/pull/2860
Patch0:         0001-fix-only-building-gtk3.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-python2
BuildOption(conf):  --disable-gtk2
BuildOption(conf):  --disable-gtk4
BuildOption(conf):  --enable-gtk3
BuildOption(conf):  --enable-wayland
BuildOption(conf):  --enable-introspection
# We don't have these dependencies now
BuildOption(conf):  --disable-dconf
BuildOption(conf):  --disable-appindicator
BuildOption(conf):  --disable-emoji-dict
# These tests need GUI environment
BuildOption(check):  DISABLE_GUI_TESTS="ibus-compose ibus-keypress test-stress xkb-latin-layouts"

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  unicode-ucd
BuildRequires:  automake
BuildRequires:  vala

%description
IBus means Intelligent Input Bus. It is an input framework for Linux OS.

%package        devel
Summary:        Development tools for ibus
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The ibus-devel package contains the header files and developer
docs for ibus.

%package        doc
Summary:        Documents for IBus
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
The ibus-doc package contains the documentation for ibus.

%package        setup
Summary:        IBus setup utility
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    setup
This is a setup utility for IBus.

%conf -a
# https://github.com/ibus/ibus/issues/2767
make -C ui/gtk3 maintainer-clean-generic

%install -a
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name}10 --generate-subpackages

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/ibus-1.0.pc
%{_includedir}/ibus-1.0/*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/IBus*-1.0.typelib
%{_datadir}/gettext/its/ibus.*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/IBus*-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/ibus-*1.0.vapi
%{_datadir}/vala/vapi/ibus-*1.0.deps

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*

%files setup
%{_bindir}/ibus-setup
%{_datadir}/applications/org.freedesktop.IBus.Setup.desktop
%{_datadir}/ibus/setup
%{_datadir}/man/man1/ibus-setup.1.gz

%files -f %{name}10.lang
%license COPYING
%{_bindir}/ibus
%{_bindir}/ibus-daemon
%{_libdir}/libibus-1.0.so.*
%{_libdir}/gtk-3.0/3.0.0/immodules/im-ibus.so
%{_prefix}/lib/systemd/user/gnome-session.target.wants/*.service
%{_mandir}/man1/ibus.1.gz
%{_mandir}/man1/ibus-daemon.1.gz
%dir %{_sysconfdir}/xdg/Xwayland-session.d
%{_sysconfdir}/xdg/Xwayland-session.d/10-ibus-x11
%{_prefix}/lib/systemd/user/org.freedesktop.IBus.session.*.service
%{_libexecdir}/ibus-engine-simple
%{_libexecdir}/ibus-portal
%{_libexecdir}/ibus-ui-gtk3
%{_libexecdir}/ibus-wayland
%{_libexecdir}/ibus-x11
%{_datadir}/applications/org.freedesktop.IBus.Panel.Wayland.Gtk3.desktop
%{_datadir}/bash-completion/completions/ibus.bash
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/ibus
%{_datadir}/ibus/component
%{_datadir}/ibus/dicts
%{_datadir}/ibus/keymaps
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
