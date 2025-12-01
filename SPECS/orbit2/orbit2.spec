# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           orbit2
Version:        2.14.19
Release:        %autorelease
Summary:        A high-performance CORBA Object Request Broker
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/Distrotech/ORBit2
#!RemoteAsset
Source:         https://download.gnome.org/sources/ORBit2/2.14/ORBit2-%{version}.tar.gz
BuildSystem:    autotools
Patch0:         0001-ORBit2-2.14.3-multilib.patch
# handle ref leaks in the a11y stack more gracefully
Patch1:         0002-ORBit2-2.14.3-ref-leaks.patch
# Guarantees the .deps directory is available for dependency tracking to build successfully.
Patch2:         0003-ORBit2-make-j-safety.patch
# Enables use of deprecated functions by removing the DG_DISABLE_DEPRECATED flag.
Patch3:         0004-ORBit2-allow-deprecated.patch
# changes all test main() functions to standard int main(void) to build successfully.
Patch4:         0005-ORBit2-configure-c99.patch
# Cast the type of pointer to to build successfully.
Patch5:         0006-pointer-type.patch

BuildOption(conf): --disable-gtk-doc
BuildOption(conf): --enable-purify
BuildOption(conf): --disable-static
BuildOption(conf): --disable-rpath

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.0
BuildRequires:  pkgconfig(libIDL-2.0) >= 0.8.0
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath

%description
ORBit is a high-performance CORBA ORB. It allows programs to send requests
and receive replies from other programs, regardless of their locations.

%package        devel
Summary:        Development libraries, header files and utilities for ORBit
Requires:       %{name} = %{version}
Requires:       indent libidl-devel  glib-devel
Requires:       pkgconfig automake

%description    devel
This package contains the header files, libraries and utilities necessary
to write programs that use CORBA technology.

%install -a
rm -f %{buildroot}%{_libdir}/ORBit-2.0/*.*a
rm -f %{buildroot}%{_libdir}/orbit-2.0/*.*a

chrpath --delete %{buildroot}%{_libdir}/libORBitCosNaming-2.so.0.1.0
chrpath --delete %{buildroot}%{_libdir}/libORBit-imodule-2.so.0.0.0
chrpath --delete %{buildroot}%{_libdir}/orbit-2.0/Everything_module.so
chrpath --delete %{buildroot}%{_bindir}/ior-decode-2
chrpath --delete %{buildroot}%{_bindir}/typelib-dump

%files
%doc AUTHORS COPYING README TODO
%{_libdir}/*.so.*
%dir %{_libdir}/orbit-2.0
%{_libdir}/orbit-2.0/*.so*

%files devel
%{_libdir}/*.so
# this is needed by libbonobo
%{_libdir}/libname-server-2.a
%{_libdir}/pkgconfig/*
%{_bindir}/orbit-idl-2
%{_bindir}/typelib-dump
%{_bindir}/orbit2-config
%{_bindir}/ior-decode-2
%{_includedir}/*
%{_datadir}/aclocal/*
%{_datadir}/idl/orbit-2.0
%{_bindir}/linc-cleanup-sockets
%{_datadir}/gtk-doc

%changelog
%{?autochangelog}
