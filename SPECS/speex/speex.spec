# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           speex
Version:        1.2.1
Release:        %autorelease
Summary:        A Free Codec For Free Speech
License:        BSD-3-Clause
URL:            http://www.speex.org/
VCS:            git:https://gitlab.xiph.org/xiph/speex.git
#!RemoteAsset
Source0:        https://downloads.xiph.org/releases/speex/speex-%{version}.tar.gz

BuildSystem:    autotools
BuildOption(conf): --enable-binaries
BuildOption(conf): --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(speexdsp)

%description
Speex is a patent-free, Open Source/Free Software voice codec.
Unlike other codecs like MP3 and Ogg Vorbis, It is designed
to compress voice at bitrates in the 2-45 kbps range. Possible
applications include VoIP, internet audio streaming, archiving
of speech data (e.g. voice mail), and audio books. It aims to
be complementary to the Vorbis codec.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%build -p
# Remove rpath from speexenc and speexdec
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install -a
# remove duped documents
rm -rf %{buildroot}%{_docdir}/speex*

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO README
%{_libdir}/libspeex.so.1*
%{_bindir}/speexenc
%{_bindir}/speexdec
%{_mandir}/man1/speexenc.1.gz
%{_mandir}/man1/speexdec.1.gz

%files devel
%doc doc/manual.pdf
%{_includedir}/speex
%{_libdir}/libspeex.so
%{_libdir}/pkgconfig/speex.pc
%{_datadir}/aclocal/speex.m4

%changelog
%{?autochangelog}
