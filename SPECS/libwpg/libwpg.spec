# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libwpg
Version:        0.3.4
Release:        %autorelease
Summary:        WordPerfect Graphics import library
License:        MPL-2.0
URL:            https://libwpg.sourceforge.net/
VCS:            git:https://git.code.sf.net/p/libwpg/code
#!RemoteAsset:  sha256:b55fda9440d1e070630eb2487d8b8697cf412c214a27caee9df69cec7c004de3
Source0:        https://downloads.sourceforge.net/libwpg/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libwpd-0.10)

%description
libwpg reads WordPerfect Graphics files. Its utilities convert
graphics to SVG and print their drawing commands.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/wpg2raw
%{_bindir}/wpg2svg
%{_bindir}/wpg2svgbatch.pl
%{_libdir}/libwpg-0.3.so.*

%files devel
%{_includedir}/libwpg-0.3/
%{_libdir}/libwpg-0.3.so
%{_libdir}/pkgconfig/libwpg-0.3.pc

%changelog
%autochangelog
