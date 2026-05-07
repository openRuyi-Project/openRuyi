# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global glib_version 2.56.0

Name:           gdk-pixbuf
Version:        2.44.6
Release:        %autorelease
Summary:        An image loading library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gdk-pixbuf
#!RemoteAsset:  sha256:140c2d0b899fcf853ee92b26373c9dc228dbcde0820a4246693f4328a27466fa
Source0:        https://download.gnome.org/sources/gdk-pixbuf/2.44/gdk-pixbuf-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgtk_doc=true
BuildOption(conf):  -Dman=true
BuildOption(conf):  -Dothers=enabled
BuildOption(conf):  -Dandroid=disabled
BuildOption(conf):  -Dglycin=disabled

BuildRequires:  docbook-xsl
BuildRequires:  gettext
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
# BuildRequires:  pkgconfig(glycin-2) >= 2.0.1
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  shared-mime-info
BuildRequires:  python3-docutils

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

%package        devel
Summary:        Development files for gdk-pixbuf
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib-devel%{?_isa} >= %{glib_version}

%description    devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%install -a
rm -rf %{buildroot}%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%transfiletriggerin -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders --update-cache

%transfiletriggerpostun -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders --update-cache

# TODO: Fix tests
%check

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_libdir}/libgdk_pixbuf-2.0.so.*
%{_libdir}/girepository-1.0
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.so
%ghost %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{_bindir}/gdk-pixbuf-query-loaders
%{_bindir}/gdk-pixbuf-thumbnailer
%{_datadir}/thumbnailers/
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*

%files devel
%dir %{_includedir}/gdk-pixbuf-2.0
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf
%{_libdir}/libgdk_pixbuf-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_datadir}/gir-1.0/
%{_mandir}/man1/gdk-pixbuf-csource.1*
%doc %{_datadir}/doc/gdk-pixbuf/
%doc %{_datadir}/doc/gdk-pixdata/

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
%autochangelog
