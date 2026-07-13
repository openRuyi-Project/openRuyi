# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ghostscript
Version:        10.07.1
Release:        %autorelease
Summary:        Interpreter for PostScript and PDF
License:        AGPL-3.0-or-later AND MIT AND Apache-2.0
URL:            https://ghostscript.com/
VCS:            git:https://github.com/ArtifexSoftware/ghostpdl.git
#!RemoteAsset:  sha256:1cdb766de8db8f1e589c817f09c5855ea5f65dfc8540e465a69ac14c18416025
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10071/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-compile-inits
BuildOption(conf):  --disable-gtk
BuildOption(conf):  --enable-cups
BuildOption(conf):  --enable-fontconfig
BuildOption(conf):  --enable-openjpeg
BuildOption(conf):  --with-drivers=ALL
BuildOption(conf):  --with-ijs
BuildOption(conf):  --with-jbig2dec
BuildOption(conf):  --with-libpaper
BuildOption(conf):  --with-system-libtiff
BuildOption(conf):  --without-local-brotli
BuildOption(conf):  --without-local-zlib
BuildOption(conf):  --without-tesseract
BuildOption(conf):  --without-versioned-path
BuildOption(conf):  --without-x
BuildOption(build):  so
BuildOption(install):  soinstall

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpaper-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  poppler-data
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jbig2dec)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)

Requires:       poppler-data

%description
Ghostscript is an interpreter and rendering engine for PostScript and PDF.
It provides command-line tools and a shared library for displaying, printing,
and converting documents.

%package        devel
Summary:        Development files for Ghostscript
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and linker file needed to build software
against the Ghostscript library.

%prep -a
# Use system libraries; openRuyi does not provide IJS separately.
rm -rf brotli cups/libs freetype jbig2dec jpeg lcms2mt leptonica libpng openjpeg tesseract tiff zlib
rm -rf Resource/CMap

%install -a
mv -f %{buildroot}%{_bindir}/{gsc,gs}
ln -s gs %{buildroot}%{_bindir}/ghostscript
rm -f %{buildroot}%{_bindir}/{lprsetup.sh,unix-lpr.sh}
# X is disabled, and dvipdf requires the unavailable dvips backend.
rm -f %{buildroot}%{_bindir}/{dvipdf,gsx}
rm -f %{buildroot}%{_mandir}/man1/dvipdf.1
rm -f %{buildroot}%{_docdir}/%{name}/COPYING
# Flatten poppler-data collections for Ghostscript resource lookup.
install -d %{buildroot}%{_datadir}/%{name}/Resource/CMap
find %{_datadir}/poppler/cMap -type f | while read -r cmap; do
    collection=${cmap#%{_datadir}/poppler/cMap/}
    ln -sf "../../../poppler/cMap/$collection" \
        "%{buildroot}%{_datadir}/%{name}/Resource/CMap/${cmap##*/}"
done

%files
%doc %{_docdir}/ghostscript/
%license LICENSE doc/COPYING DroidSansFallback.NOTICE ijs/README
%{_bindir}/*
%{_libdir}/libgs.so.10*
%{_datadir}/ghostscript/Resource/
%{_datadir}/ghostscript/iccprofiles/
%{_datadir}/ghostscript/lib/
%{_mandir}/man1/*

%files devel
%{_includedir}/ghostscript/
%{_libdir}/libgs.so

%changelog
%autochangelog
