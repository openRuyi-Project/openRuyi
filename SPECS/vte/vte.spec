# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _apiver  2.91
%define _apiver4 3.91
%define _name    vte

%bcond gtk4_support 0
%bcond glade_support 0

Name:           vte
Version:        0.82.3
Release:        %autorelease
Summary:        Terminal Emulator Library
License:        CC-BY-4.0 AND LGPL-3.0-or-later AND GPL-3.0-or-later AND MIT
URL:            https://wiki.gnome.org/Apps/Terminal/VTE
VCS:            git:https://gitlab.gnome.org/GNOME/vte.git
#!RemoteAsset
Source:         https://download.gnome.org/sources/vte/0.82/vte-0.82.3.tar.xz
BuildSystem:    meson

# PATCH-FIX-OPENSUSE: enable PIE flag to be compatible with gcc default linking option
Patch0:         0001-vte-enable-build-flag-pie.patch

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(conf):  -Ddocs=true
BuildOption(conf):  -Dgtk3=true
%if %{with gtk4_support}
BuildOption(conf):  -Dgtk4=true
%else
BuildOption(conf):  -Dgtk4=false
%endif
%if %{with glade_support}
BuildOption(conf):  -Dglade=true
%else
BuildOption(conf):  -Dglade=false
%endif

BuildRequires:  fast_float-devel
%if %{with glade_support}
BuildRequires:  glade
%endif
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gperf
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fmt) >= 11.0.0
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.7
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.0
%if %{with gtk4_support}
BuildRequires:  pkgconfig(gtk4) >= 4.14.0
%endif
BuildRequires:  pkgconfig(liblz4) >= 1.9
BuildRequires:  pkgconfig(libpcre2-8) >= 10.21
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(simdutf) >= 6.2.0
BuildRequires:  pkgconfig(vapigen) >= 0.24
BuildRequires:  pkgconfig(zlib)

%description
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package        typelib
Summary:        Introspection bindings for the VTE terminal emulator library
License:        LGPL-2.0-only

%description    typelib
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides the GObject Introspection bindings for VTE.

%package        tools
Summary:        Tools from the VTE terminal emulator package
License:        LGPL-2.0-only

%description    tools
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides tools using VTE.

%if %{with gtk4_support}
%package        typelib-gtk4
Summary:        Introspection bindings for the VTE terminal emulator library
License:        LGPL-2.0-only

%description    typelib-gtk4
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides the GObject Introspection bindings for VTE.

%package        tools-gtk4
Summary:        Tools from the VTE terminal emulator package
License:        LGPL-2.0-only

%description    tools-gtk4
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides tools using VTE.
%endif

%package        devel
Summary:        Development files for the VTE terminal emulator library
License:        LGPL-2.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-typelib = %{version}-%{release}
%if %{with gtk4_support}
Requires:       %{name}-typelib-gtk4 = %{version}-%{release}
%endif
Provides:       vte-doc = %{version}
Obsoletes:      vte-doc < %{version}

%description    devel
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package contains the files needed for building applications using
VTE.

%if %{with glade_support}
%package        glade
Summary:        Glade catalog for vte
License:        CC-BY-4.0 AND LGPL-3.0-or-later AND GPL-3.0-or-later AND MIT
Requires:       %{name} = %{version}
Requires:       glade
Supplements:    (glade and %{name}-devel)
BuildArch:      noarch

%description    glade
This package provides a catalog for Glade, to allow the use the vte
widgets in Glade.
%endif

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang vte-%{_apiver} --generate-subpackages

%files -f vte-%{_apiver}.lang
%license COPYING.CC-BY-4-0 COPYING.GPL3 COPYING.LGPL3 COPYING.XTERM
# vte libs
%{_libdir}/*.so.*
%config %{_sysconfdir}/profile.d/vte.sh
%config %{_sysconfdir}/profile.d/vte.csh
%dir %{_userunitdir}/vte-spawn-.scope.d
%{_userunitdir}/vte-spawn-.scope.d/defaults.conf
%{_libexecdir}/vte-urlencode-cwd
%dir %{_datadir}/xdg-terminals

%files typelib
%{_libdir}/girepository-1.0/Vte-%{_apiver}.typelib

%files tools
%{_bindir}/vte-%{?_apiver}
%{_datadir}/applications/org.gnome.Vte.App.Gtk3.desktop
%{_datadir}/xdg-terminals/org.gnome.Vte.App.Gtk3.desktop

%if %{with gtk4_support}
%files typelib-gtk4
%{_libdir}/girepository-1.0/Vte-%{_apiver4}.typelib

%files tools-gtk4
%{_bindir}/vte-%{?_apiver}-gtk4
%{_datadir}/applications/org.gnome.Vte.App.Gtk4.desktop
%{_datadir}/xdg-terminals/org.gnome.Vte.App.Gtk4.desktop
%endif

%files devel
%doc AUTHORS
%doc %{_docdir}/vte-%{_apiver}/
%{_libdir}/pkgconfig/vte-2.91.pc
%{_libdir}/*.so
%{_includedir}/vte-%{_apiver}/
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/vte-%{_apiver}.vapi
%{_datadir}/vala/vapi/vte-%{_apiver}.deps
%if %{with gtk4_support}
%{_includedir}/vte-%{_apiver}-gtk4/
%doc %{_docdir}/vte-%{_apiver}-gtk4/
%{_datadir}/vala/vapi/vte-%{_apiver}-gtk4.deps
%{_datadir}/vala/vapi/vte-%{_apiver}-gtk4.vapi
%endif

%if %{with glade_support}
%files glade
%{_datadir}/glade/catalogs/vte-%{_apiver}.xml
%{_datadir}/glade/pixmaps/hicolor/16x16/actions/widget-vte-terminal.png
%{_datadir}/glade/pixmaps/hicolor/22x22/actions/widget-vte-terminal.png
%endif

%changelog
%autochangelog
