# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libidl
Version:        0.8.14
Release:        %autorelease
Summary:        Library for parsing IDL (Interface Definition Language)
License:        LGPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://download.gnome.org/sources/libIDL/0.8/
VCS:            git:https://gitlab.gnome.org/Archive/libidl.git
#!RemoteAsset
Source0:        https://download.gnome.org/sources/libIDL/0.8/libIDL-%{version}.tar.bz2
Source1:        libIDL-config-2.1
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  texinfo

%description
libIDL is a library for parsing IDL (Interface Definition Language), used by
projects like ORBit2. It can be used for both COM-style and CORBA-style IDL.

%package        devel
Summary:        Development files for libIDL
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)

%description    devel
This package contains the header files, libraries, documentation, and tools
needed to develop applications that use libIDL.

%conf -p
autoreconf -fiv

%build -a
# We re-generate the info page, and also build PDF and HTML docs from the
# texinfo source.
rm libIDL2.info
make libIDL2.info libIDL2.html

%install -a
install -D -p -m 0644 -t '%{buildroot}%{_datadir}/aclocal' libIDL.m4
install -D -p -m 0644 '%{SOURCE1}' '%{buildroot}%{_mandir}/man1/libIDL-config-2.1'
install -d '%{buildroot}%{_docdir}/%{name}/html'
cp -rp libIDL2.html/* '%{buildroot}%{_docdir}/%{name}/html/'

%files
%license COPYING
%{_libdir}/libIDL-2.so.0*
%{_infodir}/libIDL2.info*
%{_docdir}/libidl/

%files devel
%doc AUTHORS BUGS ChangeLog HACKING MAINTAINERS NEWS README
%{_libdir}/libIDL-2.so
%{_includedir}/libIDL-2.0/
%{_libdir}/pkgconfig/libIDL-2.0.pc
%{_datadir}/aclocal/libIDL.m4
%{_bindir}/libIDL-config-2
%{_mandir}/man1/libIDL-config-2.1*

%changelog
%autochangelog
