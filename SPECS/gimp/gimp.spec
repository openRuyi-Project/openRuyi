# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global api_version 3.0
%global bin_version 3.2

Name:           gimp
Version:        3.2.0
Release:        %autorelease
Summary:        GNU Image Manipulation Program
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0
URL:            https://www.gimp.org
VCS:            git:https://gitlab.gnome.org/GNOME/gimp.git
#!RemoteAsset:  sha256:2618391416e51be3c693df9ef90e3860ed72ab3d36363ea1f196e30b75b2e083
Source0:        https://download.gimp.org/gimp/v3.2/gimp-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Denable-default-bin=enabled
# We don't have the dependencies in openRuyi
BuildOption(conf):  -Daa=disabled
BuildOption(conf):  -Dxpm=disabled
BuildOption(conf):  -Dilbm=disabled
BuildOption(conf):  -Dmng=disabled
BuildOption(conf):  -Dwmf=disabled
BuildOption(conf):  -Dfits=disabled
# We don't have xvfb-run
BuildOption(conf):  -Dheadless-tests=disabled
# Needs network access
BuildOption(conf):  -Dappdata-test=disabled
# The libgimp image/export tests require an installed system font
BuildOption(check):  --no-suite libgimp

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  libxslt
BuildRequires:  gi-docgen
BuildRequires:  glib-networking
BuildRequires:  ghostscript-devel
BuildRequires:  openexr-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(atk) >= 2.4.0
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.118
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.66
BuildRequires:  pkgconfig(exiv2) >= 0.27.4
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(harfbuzz) >= 2.8.2
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libmypaint) >= 1.5.0
BuildRequires:  pkgconfig(mypaint-brushes-2.0)
BuildRequires:  pkgconfig(pango) >= 1.50.0
BuildRequires:  pkgconfig(pangocairo) >= 1.50.0
BuildRequires:  pkgconfig(pangoft2) >= 1.50.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(appstream) >= 0.16.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-data)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3dist(pygobject)

Requires:       glib-networking
Requires:       python3dist(pygobject)
Requires:       mypaint-brushes

%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and
editing program, which can be extremely useful for creating logos and other
graphics for web pages. GIMP has many of the tools and filters you would expect
to find in similar commercial offerings, and some interesting extras as well.
GIMP provides a large image manipulation toolbox, including channel operations
and layers, effects, sub-pixel imaging and anti-aliasing, and conversions, all
with multi-level undo.

%package        devel
Summary:        GIMP development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The gimp-devel package contains the files needed for writing GNU Image
Manipulation Program (GIMP) plug-ins and extensions.

%install -a
# install default binary symlinks and man pages
ln -snf gimp-%{bin_version} %{buildroot}%{_bindir}/gimp
ln -snf gimp-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimp.1
ln -snf gimp-console-%{bin_version} %{buildroot}/%{_bindir}/gimp-console
ln -snf gimp-console-%{bin_version}.1 %{buildroot}/%{_mandir}/man1/gimp-console.1
ln -snf gimptool-%{bin_version} %{buildroot}%{_bindir}/gimptool
ln -snf gimptool-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimptool.1
ln -snf gimprc-%{bin_version}.5 %{buildroot}/%{_mandir}/man5/gimprc.5

%find_lang %{name}30
%find_lang %{name}30-std-plug-ins
%find_lang %{name}30-script-fu
%find_lang %{name}30-libgimp
%find_lang %{name}30-python

cat gimp30.lang gimp30-std-plug-ins.lang gimp30-script-fu.lang gimp30-libgimp.lang gimp30-python.lang > gimp-all.lang

# Automatically collect runtime plugin/module files because api_version may change.
find %{buildroot}%{_libdir}/gimp/%{api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files

cat gimp-all.lang gimp-plugin-files > gimp.files

rm -rf devel-docs/gimp-%{api_version}
mv %{buildroot}%{_docdir}/gimp-%{api_version} devel-docs

%files devel
%{_bindir}/gimptool
%{_bindir}/gimptool-3
%{_bindir}/gimptool-%{bin_version}
%{_includedir}/gimp-3.0
%{_libdir}/libgimp*.so
%{_libdir}/pkgconfig/gimp*.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gimp*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gimp*.deps
%{_datadir}/vala/vapi/gimp*.vapi
%{_mandir}/man1/gimptool.1*
%{_mandir}/man1/gimptool-3.1*
%{_mandir}/man1/gimptool-%{bin_version}.1*
%doc devel-docs/*

%files -f gimp.files
%doc AUTHORS NEWS README
%license LICENSE COPYING
%{_bindir}/gimp
%{_bindir}/gimp-script-fu-interpreter-%{api_version}
%{_bindir}/gimp-test-clipboard
%{_bindir}/gimp-test-clipboard-3
%{_bindir}/gimp-test-clipboard-%{bin_version}
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gimp-%{bin_version}
%dir %{_datadir}/gimp
%{_datadir}/gimp/%{api_version}/dynamics/
%{_datadir}/gimp/%{api_version}/file-raw/
%{_datadir}/gimp/%{api_version}/menus/
%{_datadir}/gimp/%{api_version}/tags/
%{_datadir}/gimp/%{api_version}/tips/
%{_datadir}/gimp/%{api_version}/tool-presets/
%{_datadir}/gimp/%{api_version}/brushes/
%{_datadir}/gimp/%{api_version}/fractalexplorer/
%{_datadir}/gimp/%{api_version}/gfig/
%{_datadir}/gimp/%{api_version}/gflare/
%{_datadir}/gimp/%{api_version}/gimpressionist/
%{_datadir}/gimp/%{api_version}/gradients/
%{_datadir}/gimp/%{api_version}/icons/
%{_datadir}/gimp/%{api_version}/images/
%{_datadir}/gimp/%{api_version}/palettes/
%{_datadir}/gimp/%{api_version}/patterns/
%{_datadir}/gimp/%{api_version}/scripts/
%{_datadir}/gimp/%{api_version}/themes/
%{_datadir}/gimp/%{api_version}/gimp-release
%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/%{api_version}
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/controllerrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/gimp.css
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/gimprc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/unitrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/sessionrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/templaterc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/toolrc
%{_bindir}/gimp-%{bin_version}
%{_bindir}/gimp-console-%{bin_version}
%{_bindir}/gimp-console
%{_bindir}/gimp-3
%{_bindir}/gimp-console-3
%{_libexecdir}/gimp-debug-tool
%{_libexecdir}/gimp-debug-tool-3
%{_libexecdir}/gimp-debug-tool-%{bin_version}
%{_datadir}/icons/hicolor/*/apps/gimp.png
%{_datadir}/icons/hicolor/scalable/apps/gimp.svg
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-3.1*
%{_mandir}/man1/gimp-%{bin_version}.1*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man1/gimp-console-3.1*
%{_mandir}/man1/gimp-console-%{bin_version}.1*
%{_mandir}/man5/gimprc*.5*
%{_libdir}/libgimp*.so.*
%{_libdir}/girepository-1.0/Gimp*.typelib

%changelog
%autochangelog
