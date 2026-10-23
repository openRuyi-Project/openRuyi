# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libical
Version:        4.0.7
Release:        %autorelease
Summary:        Reference implementation of the iCalendar data type and serialization format
License:        (LGPL-2.1-only OR MPL-2.0) AND BSD-3-Clause
URL:            https://libical.github.io/libical/
VCS:            git:https://github.com/libical/libical
#!RemoteAsset:  sha256:47c05bc96e41416578cf1803bb2ba3f8d292cb17d5ac2fca539dee922bae8a94
Source:         https://github.com/libical/libical/archive/v%{version}/libical-%{version}.tar.gz
BuildSystem:    cmake

# Preserve the libical.pc link interface used by BlueZ's vCard backend.
Patch2000:      2000-keep-legacy-pkg-config-libraries.patch

# Share generated GIR and typelib rules across parallel Vala targets.
BuildOption(conf):  -G Ninja
BuildOption(conf):  -DLIBICAL_GOBJECT_INTROSPECTION:BOOL=ON
BuildOption(conf):  -DLIBICAL_GLIB:BOOL=ON
BuildOption(conf):  -DLIBICAL_GLIB_VAPI:BOOL=ON
BuildOption(conf):  -DLIBICAL_JAVA_BINDINGS:BOOL=OFF
BuildOption(conf):  -DLIBICAL_BUILD_DOCS:BOOL=OFF
BuildOption(conf):  -DLIBICAL_GLIB_BUILD_DOCS:BOOL=OFF
BuildOption(conf):  -DLIBICAL_BUILD_TESTING:BOOL=ON

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(python3)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  python3
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(setuptools)
BuildRequires:  vala

Requires:       tzdata

%description
Reference implementation of the iCalendar data type and serialization format
used in dozens of calendaring and scheduling products.

%package        devel
Summary:        Development files for libical
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libical-devel package contains libraries and header files for developing
applications that use libical.

%package        glib
Summary:        GObject wrapper for libical library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    glib
This package provides a GObject wrapper for libical library with support
of GObject Introspection.

%package        glib-devel
Summary:        Development files for building against %{name}-glib
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-glib = %{version}-%{release}

%description    glib-devel
Development files needed for building things which link against %{name}-glib.

%files
%doc README.md CHANGELOG.md CONTRIBUTORS.md
%license LICENSE.txt COPYING.LESSER.txt LICENSES/BSD-3-Clause.txt LICENSES/MPL-2.0.txt
%{_libdir}/libical.so.4.0
%{_libdir}/libical.so.%{version}
%{_libdir}/libical_cxx.so.4.0
%{_libdir}/libical_cxx.so.%{version}
%{_libdir}/libicalss.so.4.0
%{_libdir}/libicalss.so.%{version}
%{_libdir}/libicalss_cxx.so.4.0
%{_libdir}/libicalss_cxx.so.%{version}
%{_libdir}/libicalvcal.so.4.0
%{_libdir}/libicalvcal.so.%{version}
%{_libdir}/libicalvcard.so.4.0
%{_libdir}/libicalvcard.so.%{version}
%{_libdir}/girepository-1.0/ICal-4.0.typelib

%files devel
%{_libdir}/libical.so
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss.so
%{_libdir}/libicalss_cxx.so
%{_libdir}/libicalvcal.so
%{_libdir}/libicalvcard.so
%{_libdir}/pkgconfig/libical.pc
%{_libdir}/pkgconfig/libicalss.pc
%{_libdir}/pkgconfig/libicalvcal.pc
%{_libdir}/pkgconfig/libicalvcard.pc
%{_libdir}/cmake/LibIcal/
%{_includedir}/libical/
%{_datadir}/gir-1.0/ICal-4.0.gir
%{_libexecdir}/libical/ical-glib-src-generator

%files glib
%{_libdir}/libical-glib.so.4.0
%{_libdir}/libical-glib.so.%{version}
%{_libdir}/girepository-1.0/ICalGLib-4.0.typelib

%files glib-devel
%{_libdir}/libical-glib.so
%{_libdir}/pkgconfig/libical-glib.pc
%{_includedir}/libical-glib/
%{_datadir}/gir-1.0/ICalGLib-4.0.gir
%{_datadir}/vala/vapi/libical-glib.vapi

%changelog
%autochangelog
