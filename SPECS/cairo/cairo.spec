# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change these to 1 once we have them
%bcond gtk_doc 0

Name:           cairo
Version:        1.18.4
Release:        %autorelease
Summary:        A 2D graphics library
License:        LGPL-2.1-only OR MPL-1.1
URL:            https://cairographics.org
VCS:            git:git://anongit.freedesktop.org/git/cairo
#!RemoteAsset
Source0:        https://cairographics.org/releases/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dfreetype=enabled
BuildOption(conf):  -Dfontconfig=enabled
BuildOption(conf):  -Dglib=enabled
%if %{with gtk_doc}
BuildOption(conf):  -Dgtk_doc=true
%endif
BuildOption(conf):  -Dspectre=disabled
BuildOption(conf):  -Dsymbol-lookup=disabled
BuildOption(conf):  -Dtee=enabled
BuildOption(conf):  -Dtests=disabled
BuildOption(conf):  -Dxcb=enabled
BuildOption(conf):  -Dxlib=enabled

BuildRequires:  meson
%if %{with gtk_doc}
BuildRequires:  gtk-doc
%endif
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xrender)

%description
Cairo is a 2D graphics library designed to provide high-quality display
and print output. Currently supported output targets include the X Window
System, in-memory image buffers, and image files (PDF, PostScript, and SVG).

Cairo is designed to produce consistent output on all output media while
taking advantage of display hardware acceleration when available.

%package        devel
Summary:        Development files for cairo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo graphics library.

%package        gobject
Summary:        GObject bindings for cairo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gobject
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains functionality to make cairo graphics library
integrate well with the GObject object system used by GNOME.

%package         gobject-devel
Summary:         Development files for cairo-gobject
Requires:        %{name}-devel%{?_isa} = %{version}-%{release}
Requires:        %{name}-gobject%{?_isa} = %{version}-%{release}

%description    gobject-devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.

%package        tools
Summary:        Development tools for cairo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains tools for working with the cairo graphics library.
 * cairo-trace: Record cairo library calls for later playback

%files
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc AUTHORS BUGS NEWS README.md
%{_libdir}/libcairo.so.2*
%{_libdir}/libcairo-script-interpreter.so.2*

%files devel
%dir %{_includedir}/cairo/
%{_includedir}/cairo/cairo-deprecated.h
%{_includedir}/cairo/cairo-features.h
%{_includedir}/cairo/cairo-ft.h
%{_includedir}/cairo/cairo.h
%{_includedir}/cairo/cairo-pdf.h
%{_includedir}/cairo/cairo-ps.h
%{_includedir}/cairo/cairo-script-interpreter.h
%{_includedir}/cairo/cairo-svg.h
%{_includedir}/cairo/cairo-tee.h
%{_includedir}/cairo/cairo-version.h
%{_includedir}/cairo/cairo-xlib-xrender.h
%{_includedir}/cairo/cairo-xlib.h
%{_includedir}/cairo/cairo-script.h
%{_includedir}/cairo/cairo-xcb.h
%{_libdir}/libcairo.so
%{_libdir}/libcairo-script-interpreter.so
%{_libdir}/pkgconfig/cairo-fc.pc
%{_libdir}/pkgconfig/cairo-ft.pc
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-pdf.pc
%{_libdir}/pkgconfig/cairo-png.pc
%{_libdir}/pkgconfig/cairo-ps.pc
%{_libdir}/pkgconfig/cairo-script-interpreter.pc
%{_libdir}/pkgconfig/cairo-svg.pc
%{_libdir}/pkgconfig/cairo-tee.pc
%{_libdir}/pkgconfig/cairo-xlib.pc
%{_libdir}/pkgconfig/cairo-xlib-xrender.pc
%{_libdir}/pkgconfig/cairo-script.pc
%{_libdir}/pkgconfig/cairo-xcb-shm.pc
%{_libdir}/pkgconfig/cairo-xcb.pc
%if %{with gtk_doc}
%{_datadir}/gtk-doc/html/cairo
%endif

%files gobject
%{_libdir}/libcairo-gobject.so.2*

%files gobject-devel
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc

%files tools
%{_bindir}/cairo-trace
%{_libdir}/cairo/

%changelog
%autochangelog
