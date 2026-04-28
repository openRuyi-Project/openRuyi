# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvorbis
Version:        1.3.7
Release:        %autorelease
Summary:        The Vorbis General Audio Compression Codec
License:        BSD-3-Clause
URL:            https://github.com/xiph/vorbis
#!RemoteAsset
Source:         https://github.com/xiph/vorbis/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ogg)

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format. This package contains runtime
libraries for Ogg Vorbis.

%package        devel
Summary:        Development tools and documentation for Vorbis
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and documentation
needed to develop applications with Ogg Vorbis.

%conf -p
./autogen.sh

%install -a
rm -f %{buildroot}%{_docdir}/%{name}-%{version}/doxygen-build.stamp

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*

%files devel
%doc %{_docdir}/libvorbis-%{version}
%{_includedir}/vorbis
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/vorbis.pc
%{_libdir}/pkgconfig/vorbisenc.pc
%{_libdir}/pkgconfig/vorbisfile.pc
%{_datadir}/aclocal/vorbis.m4

%changelog
%{?autochangelog}
