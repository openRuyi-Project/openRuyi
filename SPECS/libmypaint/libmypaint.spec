# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmypaint
Version:        1.6.1
Release:        %autorelease
Summary:        Library for making brush strokes
License:        ISC
URL:            https://github.com/mypaint/libmypaint
#!RemoteAsset:  sha256:741754f293f6b7668f941506da07cd7725629a793108bb31633fb6c3eae5315f
Source0:        https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-introspection=yes
BuildOption(conf):  --disable-gegl
BuildOption(conf):  --disable-docs

BuildRequires:  make
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.32.0
BuildRequires:  pkgconfig(json-c)

%description
This is a self-contained library containing the MyPaint brush engine.

%package        devel
Summary:        Development files for libmypaint
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and libraries needed for development
with libmypaint.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_libdir}/libmypaint.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/MyPaint-1.6.typelib

%files devel
%{_libdir}/libmypaint.so
%{_includedir}/libmypaint/
%{_libdir}/pkgconfig/libmypaint.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MyPaint-1.6.gir

%changelog
%autochangelog
