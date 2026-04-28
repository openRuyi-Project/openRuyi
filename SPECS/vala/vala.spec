# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# first two digits of version
%global release_version 0.56

# graphviz is needed only for valadoc
# Set to 1 if you want to build valadoc
%bcond graphbiz 0

Name:           vala
Version:        %{release_version}.18
Release:        %autorelease
Summary:        A modern programming language for GNOME
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/Vala
VCS:            git:https://gitlab.gnome.org/GNOME/vala.git
#!RemoteAsset:  sha256:f2affe7d40ab63db8e7b9ecc3f6bdc9c2fc7e3134c84ff2d795f482fe926a382
Source:         https://download.gnome.org/sources/vala/%{release_version}/vala-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
%if %{without graphbiz}
BuildOption(conf):  --disable-valadoc
%endif
BuildOption(conf):  lt_cv_sys_lib_search_path_spec="/lib /usr/lib /lib64 /usr/lib64"
BuildOption(conf):  lt_cv_sys_lib_dlsearch_path_spec="/lib /usr/lib /lib64 /usr/lib64"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
# for test
BuildRequires:  dbus-tools
%if %{with graphbiz}
BuildRequires:  pkgconfig(libgvc)
%endif

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.

%package        devel
Summary:        Vala compiler library & Development files for libvala

%description    devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files & shared libvala library
for libvala. This is not necessary for using the %{name} compiler.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.

%if %{with graphbiz}
%package -n     valadoc
Summary:        Vala documentation generator
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description -n valadoc
Valadoc is a documentation generator for generating API documentation from Vala
source code.

%package -n     valadoc-devel
Summary:        Development files for valadoc
Requires:       valadoc = %{version}-%{release}

%description -n valadoc-devel
Valadoc is a documentation generator for generating API documentation from Vala
source code.

The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.
%endif

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/vala
%{_bindir}/vala-%{release_version}
%{_bindir}/valac
%{_bindir}/valac-%{release_version}
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-gen-introspect-%{release_version}*
%{_bindir}/vapigen
%{_bindir}/vapigen-%{release_version}
%{_libdir}/pkgconfig/vapigen-0.56.pc
%{_libdir}/pkgconfig/vapigen.pc
%{_libdir}/vala-%{release_version}/
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/vala/
%{_datadir}/vala-%{release_version}/
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{release_version}.1*
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{release_version}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{release_version}.1*

%files devel
%{_includedir}/vala-%{release_version}
%{_libdir}/libvala-%{release_version}.so
%{_libdir}/libvala-%{release_version}.so.*
%{_libdir}/pkgconfig/libvala-%{release_version}.pc

%files doc
%doc %{_datadir}/devhelp/books/vala-%{release_version}

%if %{with graphbiz}
# TODO: check this once we have valadoc built
%files -n valadoc
%{_bindir}/valadoc
%{_bindir}/valadoc-%{release_version}
%{_libdir}/libvaladoc-%{release_version}.so.0*
%{_libdir}/valadoc-%{release_version}/
%{_datadir}/valadoc-%{release_version}/
%{_mandir}/man1/valadoc-%{release_version}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-devel
%{_includedir}/valadoc-%{release_version}/
%{_libdir}/libvaladoc-%{release_version}.so
%{_libdir}/pkgconfig/valadoc-%{release_version}.pc
%endif

%changelog
%autochangelog
