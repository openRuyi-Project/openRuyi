# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcdio-paranoia
Version:        10.2+2.0.2
Release:        %autorelease
Summary:        CD paranoia on top of libcdio
License:        GPL-3.0-or-later
URL:            https://github.com/libcdio/libcdio-paranoia
#!RemoteAsset:  sha256:186892539dedd661276014d71318c8c8f97ecb1250a86625256abd4defbf0d0c
Source0:        https://github.com/libcdio/libcdio-paranoia/releases/download/release-%{version}/libcdio-paranoia-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcdio)

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from the
CDROM directly as data, with no analog step between, and writes the
data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

Split off from libcdio to allow more flexible licensing and to be compatible
with cdparanoia-III-10.2's license.

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and libraries for %{name}.

%insatll -a
cp -a %{buildroot}%{_includedir}/cdio/paranoia/*.h %{buildroot}%{_includedir}/cdio/

%check
# skip tests as in build env.

%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*
%{_mandir}/ja/man1/*

%files devel
%doc doc/overlapdef.txt
%{_includedir}/cdio/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcdio_cdda.pc
%{_libdir}/pkgconfig/libcdio_paranoia.pc

%changelog
%autochangelog
