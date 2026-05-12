# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bin_version 3.0.0

%bcond doc 0
# No display.
%bcond tests 0

Name:           gtk3
Version:        3.24.51
Release:        %autorelease
Summary:        GTK+ graphical user interface library
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gtk
#!RemoteAsset:  sha256:0013877c6bd23c2dbe42ad7c70a053d0e449be66736574e37867c49c5f905a4f
Source0:        https://download.gnome.org/sources/gtk/3.24/gtk-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuiltin_immodules=wayland,waylandgtk
BuildOption(conf):  -Dxinerama=yes
BuildOption(conf):  -Dprint_backends=file,lpr
BuildOption(conf):  -Dbroadway_backend=false
BuildOption(conf):  -Dcolord=yes
BuildOption(conf):  -Dtracker3=true
%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
BuildOption(conf):  -Dman=true
%else
BuildOption(conf):  -Dgtk_doc=false
BuildOption(conf):  -Dman=false
%endif
%if %{with tests}
BuildOption(conf):  -Dinstalled_tests=true
BuildOption(conf):  -Dtests=true
%else
BuildOption(conf):  -Dinstalled_tests=false
BuildOption(conf):  -Dtests=false
%endif
BuildOption(conf):  -Dprofiler=false

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0) >= 2.57.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(pango) >= 1.41.0
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.0
BuildRequires:  pkgconfig(atk) >= 2.35.1
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cups-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(wayland-client) >= 1.14.91
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
%if %{with doc}
BuildRequires:  gtk-doc
%endif

Requires:       hicolor-icon-theme

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.

%package        devel
Summary:        Development files for GTK+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for GTK+.

%if %{with tests}
%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
Tests for gtk3.
%endif

%install -a
touch %{buildroot}%{_libdir}/gtk-3.0/%{bin_version}/immodules.cache
mkdir -p %{buildroot}%{_sysconfdir}/gtk-3.0
mkdir -p %{buildroot}%{_libdir}/gtk-3.0/modules
mkdir -p %{buildroot}%{_libdir}/gtk-3.0/immodules

# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang gtk30 --all-name --generate-subpackages

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%if %{with tests}
%meson_test
%endif

%transfiletriggerin -- %{_libdir}/gtk-3.0/3.0.0/immodules
%{_bindir}/gtk-query-immodules-3.0 --update-cache &>/dev/null || :

%transfiletriggerpostun -- %{_libdir}/gtk-3.0/3.0.0/immodules
%{_bindir}/gtk-query-immodules-3.0 --update-cache &>/dev/null || :

%files -f gtk30.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gtk-query-immodules-3.0*
%{_bindir}/gtk-launch
%{_libdir}/libgtk-3.so.0*
%{_libdir}/libgdk-3.so.0*
%{_libdir}/libgailutil-3.so.0*
%dir %{_libdir}/gtk-3.0
%dir %{_libdir}/gtk-3.0/%{bin_version}
%dir %{_libdir}/gtk-3.0/%{bin_version}/immodules
%{_libdir}/gtk-3.0/%{bin_version}/printbackends
%{_libdir}/gtk-3.0/modules
%{_libdir}/gtk-3.0/immodules
%{_datadir}/themes/Default
%{_datadir}/themes/Emacs
%{_libdir}/girepository-1.0/Gtk-3.0.typelib
%{_libdir}/girepository-1.0/Gdk-3.0.typelib
%{_libdir}/girepository-1.0/GdkX11-3.0.typelib
%ghost %{_libdir}/gtk-3.0/%{bin_version}/immodules.cache
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/gtk-3.0
%{_datadir}/gtk-3.0/emoji/
%if %{with broadway}
%{_bindir}/broadwayd
%endif
%{_bindir}/gtk-update-icon-cache
%{_libdir}/gtk-3.0/%{bin_version}/immodules/im-*.so
%config(noreplace) %{_sysconfdir}/gtk-3.0/im-multipress.conf

%files devel
%{_libdir}/lib*.so
%{_includedir}/gail-3.0/
%{_includedir}/gtk-3.0/
%{_datadir}/aclocal/gtk-3.0.m4
%{_libdir}/pkgconfig/gail-3.0.pc
%{_libdir}/pkgconfig/gdk-3.0.pc
%{_libdir}/pkgconfig/gdk-wayland-3.0.pc
%{_libdir}/pkgconfig/gdk-x11-3.0.pc
%{_libdir}/pkgconfig/gtk+-3.0.pc
%{_libdir}/pkgconfig/gtk+-unix-print-3.0.pc
%{_libdir}/pkgconfig/gtk+-wayland-3.0.pc
%{_libdir}/pkgconfig/gtk+-x11-3.0.pc
%{_bindir}/gtk3-*
%{_bindir}/gtk-builder-tool
%{_bindir}/gtk-encode-symbolic-svg
%{_bindir}/gtk-query-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gettext/
%{_datadir}/gir-1.0
%{_datadir}/gtk-3.0/gtkbuilder.rng
%{_datadir}/gtk-3.0/valgrind/

%if %{with tests}
%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
%endif

%changelog
%autochangelog
