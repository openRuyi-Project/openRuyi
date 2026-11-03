# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           librevenge
Version:        0.0.6
Release:        %autorelease
Summary:        Document interfaces for import filters
License:        MPL-2.0 AND BSD-3-Clause
URL:            https://sourceforge.net/p/libwpd/wiki/librevenge/
VCS:            git:https://git.code.sf.net/p/libwpd/librevenge
#!RemoteAsset:  sha256:52a65e904d255dbdd97a8b7bb28d6574e14f999eb01416aff004502406d0904d
Source0:        https://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-tests
BuildOption(conf):  --without-docs

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(zlib)

%description
librevenge provides interfaces for reading and generating text documents,
spreadsheets, presentations and vector graphics. Its stream and generator
libraries let format parsers read documents and emit converted content.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
sed -n '/^\/\* librevenge$/,/\*\//p' src/lib/RVNGOLEStream.cpp > POLE-LICENSE.txt
grep -Fq "Redistributions in binary form" POLE-LICENSE.txt

%files
%doc AUTHORS README
%license COPYING.MPL COPYING.LGPL POLE-LICENSE.txt
%{_libdir}/librevenge*-0.0.so.*

%files devel
%{_includedir}/librevenge-0.0/
%{_libdir}/librevenge*-0.0.so
%{_libdir}/pkgconfig/librevenge-0.0.pc
%{_libdir}/pkgconfig/librevenge-generators-0.0.pc
%{_libdir}/pkgconfig/librevenge-stream-0.0.pc

%changelog
%autochangelog
