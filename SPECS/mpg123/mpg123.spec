# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpg123
Version:        1.33.7
Release:        %autorelease
Summary:        Real-time MPEG 1.0/2.0/2.5 audio player and decoder library
License:        LGPL-2.1-only
URL:            https://www.mpg123.org/
VCS:            svn:svn://scm.orgis.org/mpg123/trunk
#!RemoteAsset:  sha256:31d0e35a4ca567ec9b5ebda6c3062bb4435d6d3eacd6ef0d95cadd7854dc03ee
Source0:        https://www.mpg123.org/download/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)

%description
mpg123 is a real-time MPEG 1.0/2.0/2.5 audio player for layers 1, 2, and 3,
providing libmpg123, libout123, and libsyn123 libraries and audio output plugins.

%package        libs
Summary:        Libraries for %{name}

%description    libs
This package provides the shared libraries libmpg123, libout123, and libsyn123.

%package        plugins-jack
Summary:        JACK output plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-jack
This package provides the JACK audio output plugin for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files, libraries, and pkg-config metadata
needed to develop applications that use libmpg123, libout123, or libsyn123.

%files
%doc AUTHORS NEWS NEWS.libmpg123 NEWS.libout123 NEWS.libsyn123 README
%{_bindir}/mpg123*
%{_bindir}/out123
%dir %{_libdir}/mpg123
%{_libdir}/mpg123/output_*.so
%exclude %{_libdir}/mpg123/output_jack.so
%{_mandir}/man1/mpg123.1*
%{_mandir}/man1/out123.1*

%files libs
%license COPYING
%{_libdir}/libmpg123.so.*
%{_libdir}/libout123.so.*
%{_libdir}/libsyn123.so.*

%files plugins-jack
%{_libdir}/mpg123/output_jack.so

%files devel
%{_includedir}/*.h
%{_libdir}/libmpg123.so
%{_libdir}/libout123.so
%{_libdir}/libsyn123.so
%{_libdir}/pkgconfig/libmpg123.pc
%{_libdir}/pkgconfig/libout123.pc
%{_libdir}/pkgconfig/libsyn123.pc

%changelog
%autochangelog
