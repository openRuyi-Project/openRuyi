# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorminor 1.0

%bcond cdparanoia 0
%bcond libvisual 0
%bcond doc 0
# some tests will fail,so just skip now.
%bcond tests 0

Name:           gstreamer-plugins-base
Version:        1.27.50
Release:        %autorelease
Summary:        GStreamer streaming media framework base plugins
License:        LGPL-2.1-or-later
URL:            http://gstreamer.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/gstreamer/gstreamer/-/tree/main/subprojects/gst-plugins-base
#!RemoteAsset
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dpackage-name='GStreamer-plugins-base package'
BuildOption(conf):  -Dpackage-origin='http://www.gstreamer.org'
BuildOption(conf):  -Dgl_winsys=wayland,x11,gbm
BuildOption(conf):  -Dtremor=disabled
BuildOption(conf):  -Dexamples=disabled
BuildOption(conf):  -Dxvideo=disabled
BuildOption(conf):  -Dorc=disabled
BuildOption(conf):  -Dtheora=disabled
%if %{with cdparanoia}
BuildOption(conf):  -Dcdparanoia=enabled
%else
BuildOption(conf):  -Dcdparanoia=disabled
%endif
%if %{with libvisual}
BuildOption(conf):  -Dlibvisual=enabled
%else
BuildOption(conf):  -Dlibvisual=disabled
%endif
%if %{with doc}
BuildOption(conf):  -Ddoc=enabled
%else
BuildOption(conf):  -Ddoc=disabled
%endif
%if %{with tests}
BuildOption(conf):  -Dtests=enabled
%else
BuildOption(conf):  -Dtests=disabled
%endif

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.1
BuildRequires:  iso-codes-devel
BuildRequires:  pkgconfig
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(wayland-client) >= 1.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
%if %{with cdparanoia}
BuildRequires:  pkgconfig(cdparanoia-3)
%endif
%if %{with libvisual}
BuildRequires:  pkgconfig(libvisual-0.4)
%endif

Requires:       iso-codes

%description
GStreamer is a streaming media framework. This package contains a set of
well-maintained base plug-ins.

%package        devel
Summary:        GStreamer Base Plugins Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang gst-plugins-base-%{majorminor} --generate-subpackages

%files -f gst-plugins-base-%{majorminor}.lang
%license COPYING
%doc NEWS README.md
%{_libdir}/libgstallocators-%{majorminor}.so.*
%{_libdir}/libgstaudio-%{majorminor}.so.*
%{_libdir}/libgstfft-%{majorminor}.so.*
%{_libdir}/libgstriff-%{majorminor}.so.*
%{_libdir}/libgsttag-%{majorminor}.so.*
%{_libdir}/libgstrtp-%{majorminor}.so.*
%{_libdir}/libgstvideo-%{majorminor}.so.*
%{_libdir}/libgstpbutils-%{majorminor}.so.*
%{_libdir}/libgstrtsp-%{majorminor}.so.*
%{_libdir}/libgstsdp-%{majorminor}.so.*
%{_libdir}/libgstapp-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*
%{_libdir}/girepository-1.0/Gst*-%{majorminor}.typelib
%dir %{_libdir}/gstreamer-%{majorminor}
# base plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstapp.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstbasedebug.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstdsd.so
%{_libdir}/gstreamer-%{majorminor}/libgstencoding.so
%{_libdir}/gstreamer-%{majorminor}/libgstgio.so
%{_libdir}/gstreamer-%{majorminor}/libgstoverlaycomposition.so
%{_libdir}/gstreamer-%{majorminor}/libgstplayback.so
%{_libdir}/gstreamer-%{majorminor}/libgstpbtypes.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubparse.so
%{_libdir}/gstreamer-%{majorminor}/libgsttcp.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoconvertscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstogg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopus.so
%{_libdir}/gstreamer-%{majorminor}/libgstpango.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesink.so
%if %{with cdparanoia}
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so
%endif
%if %{with libvisual}
%{_libdir}/gstreamer-%{majorminor}/libgstlibvisual.so
%endif
%{_bindir}/gst-discoverer-%{majorminor}
%{_bindir}/gst-play-%{majorminor}
%{_bindir}/gst-device-monitor-%{majorminor}
%{_mandir}/man1/gst-discoverer-*
%{_mandir}/man1/gst-play-*
%{_mandir}/man1/gst-device-monitor-*

%files devel
%{_includedir}/gstreamer-%{majorminor}/gst/*
%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/
%{_datadir}/gir-1.0/Gst*-%{majorminor}.gir
%{_libdir}/libgst*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/gst-plugins-base
%{_datadir}/gst-plugins-base/%{majorminor}/

%changelog
%autochangelog
