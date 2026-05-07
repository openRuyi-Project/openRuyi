# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvirt-glib
Version:        5.0.0
Release:        %autorelease
Summary:        libvirt glib integration for events
License:        LGPL-2.1-or-later
URL:            https://libvirt.org/
VCS:            git:https://gitlab.com/libvirt/libvirt-glib
#!RemoteAsset:  sha256:9bfec346382416a3575d87299bc641b2a464aa519fd9b1287e318aa43a2f3b8b
Source:         https://libvirt.org/sources/glib/libvirt-glib-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Drpath=disabled

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  gtk-doc

%description
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed.

%package       devel
Summary:       libvirt glib integration for events development files
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig(libvirt)

%description   devel
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc README COPYING AUTHORS NEWS
%{_libdir}/libvirt-g*-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtG*-1.0.typelib

%files devel
%doc examples/event-test.c
%{_libdir}/libvirt-g*-1.0.so
%{_libdir}/pkgconfig/libvirt-gconfig-1.0.pc
%{_libdir}/pkgconfig/libvirt-glib-1.0.pc
%{_libdir}/pkgconfig/libvirt-gobject-1.0.pc
%dir %{_includedir}/libvirt-g*-1.0
%dir %{_includedir}/libvirt-g*-1.0/libvirt-g*
%{_includedir}/*-1.0/libvirt-g*/*.h
%{_datadir}/gir-1.0/LibvirtG*-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-g*
%{_datadir}/vala/vapi/libvirt-g*

%changelog
%autochangelog
