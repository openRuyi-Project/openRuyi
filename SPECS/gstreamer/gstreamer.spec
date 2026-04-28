# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorminor 1.0
%bcond doc 0

Name:           gstreamer
Version:        1.27.50
Release:        %autorelease
Summary:        GStreamer streaming media framework runtime
License:        LGPL-2.1-or-later
URL:            http://gstreamer.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/gstreamer/
#!RemoteAsset
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
Source1:        gstreamer.prov
Source2:        gstreamer.attr
BuildSystem:    meson

BuildOption(conf):  -Dpackage-name='GStreamer package'
BuildOption(conf):  -Dpackage-origin='http://www.gstreamer.org'
BuildOption(conf):  -Dptp-helper-permissions=capabilities
BuildOption(conf):  -Ddbghelp=disabled
BuildOption(conf):  -Dlibunwind=enabled
BuildOption(conf):  -Dlibdw=enabled
BuildOption(conf):  -Dtests=enabled
%if %{with doc}
BuildOption(conf):  -Ddoc=enabled
BuildOption(conf):  -Dexamples=enabled
%else
BuildOption(conf):  -Ddoc=disabled
BuildOption(conf):  -Dexamples=disabled
%endif

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.1
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcap)
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  rust
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libdw)
%if %{with doc}
BuildRequires:  pkgconfig(gtk+-3.0)
%endif

%description
GStreamer is a streaming media framework. This package contains the core
libraries and tools.

%package        devel
Summary:        Libraries/include files for GStreamer streaming media framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libxml-2.0)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang gstreamer-%{majorminor} --generate-subpackages

install -m0755 -D %{SOURCE1} %{buildroot}%{_rpmconfigdir}/gstreamer.prov
install -m0644 -D %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/gstreamer.attr

%files -f gstreamer-%{majorminor}.lang
%license COPYING
%doc NEWS README.md
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcheck-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*
%dir %{_libexecdir}/gstreamer-%{majorminor}/
%{_libexecdir}/gstreamer-%{majorminor}/gst-completion-helper
%{_libexecdir}/gstreamer-%{majorminor}/gst-hotdoc-plugins-scanner
%{_libexecdir}/gstreamer-%{majorminor}/gst-plugins-doc-cache-generator
%{_libexecdir}/gstreamer-%{majorminor}/gst-plugin-scanner
%attr(755,root,root) %caps(cap_net_bind_service,cap_net_admin,cap_sys_nice=ep) %{_libexecdir}/gstreamer-%{majorminor}/gst-ptp-helper
%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoretracers.so
%{_libdir}/girepository-1.0/Gst*-%{majorminor}.typelib
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-stats-%{majorminor}
%{_bindir}/gst-tester-1.0
%{_bindir}/gst-typefind-%{majorminor}
%{_rpmconfigdir}/gstreamer.prov
%{_rpmconfigdir}/fileattrs/gstreamer.attr
%{_mandir}/man1/gst-*.1*
%{_datadir}/bash-completion/completions/gst-*
%{_datadir}/bash-completion/helpers/gst

%files devel
%{_includedir}/gstreamer-%{majorminor}/
%{_libdir}/libgst*.so
%{_datadir}/gir-1.0/Gst*-%{majorminor}.gir
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_datadir}/gstreamer-%{majorminor}/gdb/
%{_datadir}/gdb/auto-load/
%{_libdir}/pkgconfig/gstreamer-1.0.pc
%{_libdir}/pkgconfig/gstreamer-base-1.0.pc
%{_libdir}/pkgconfig/gstreamer-check-1.0.pc
%{_libdir}/pkgconfig/gstreamer-controller-1.0.pc
%{_libdir}/pkgconfig/gstreamer-net-1.0.pc
%{_datadir}/cmake/FindGStreamer.cmake

%changelog
%{?autochangelog}
