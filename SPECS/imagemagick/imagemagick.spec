# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           imagemagick
Version:        7.1.2.25
Release:        %autorelease
Summary:        An X application for displaying and manipulating images
License:        ImageMagick
URL:            https://github.com/ImageMagick/ImageMagick
#!RemoteAsset:  sha256:2b2070802de374871737ff1a516b3d9d1e66643779b7ed9c52e2534db7772006
Source:         https://imagemagick.org/archive/releases/ImageMagick-7.1.2-25.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --with-modules
BuildOption(conf):  --with-webp

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ddjvuapi)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
ImageMagick is an image display and manipulation tool for the X
Window System. ImageMagick can read and write JPEG, TIFF, PNM, GIF,
and Photo CD image formats. It can resize, rotate, sharpen, color
reduce, or add special effects to an image, and when finished you can
either save the completed work in the original format or a different
one. ImageMagick also includes command line programs for creating
animated or transparent .gifs, creating composite images, creating
thumbnail images, and more.

%package        doc
Summary:        ImageMagick documentation
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
ImageMagick documentation, this package contains usage (for the
commandline tools) and API (for the libraries) documentation in html format.
Note this documentation can also be found on the ImageMagick website:
http://www.imagemagick.org/

%package        devel
Summary:        Library links and header files for ImageMagick app development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
ImageMagick-devel contains the library links and header files you'll
need to develop ImageMagick applications. ImageMagick is an image
manipulation program.

%package        libs
Summary:        ImageMagick libraries to link with

%description    libs
This packages contains a shared libraries to use within other applications.

%conf -p
autoreconf -fiv

%files
%{_bindir}/animate
%{_bindir}/compare
%{_bindir}/composite
%{_bindir}/conjure
%{_bindir}/display
%{_bindir}/identify
%{_bindir}/import
%{_bindir}/magick
%{_bindir}/mogrify
%{_bindir}/montage
%{_bindir}/stream
%{_bindir}/convert
%{_bindir}/magick-script

%files doc
%doc %{_datadir}/doc/ImageMagick-7
%doc %{_mandir}/man1/*

%files devel
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/libMagickCore-7.Q16HDRI.so
%{_libdir}/libMagickWand-7.Q16HDRI.so
%{_libdir}/libMagick++-7.Q16HDRI.so
%{_libdir}/pkgconfig/MagickCore.pc
%{_libdir}/pkgconfig/MagickCore-7.Q16HDRI.pc
%{_libdir}/pkgconfig/ImageMagick.pc
%{_libdir}/pkgconfig/ImageMagick-7.Q16HDRI.pc
%{_libdir}/pkgconfig/MagickWand.pc
%{_libdir}/pkgconfig/MagickWand-7.Q16HDRI.pc
%{_libdir}/pkgconfig/Magick++-7.Q16HDRI.pc
%{_libdir}/pkgconfig/Magick++.pc
%{_includedir}/ImageMagick-7/*
%{_mandir}/man1/MagickCore-config.*
%{_mandir}/man1/MagickWand-config.*
%{_bindir}/Magick++-config

%files libs
%dir %{_sysconfdir}/ImageMagick-7
%config(noreplace) %{_sysconfdir}/ImageMagick-7/*.xml
%{_libdir}/ImageMagick-7.1.2/config-Q16HDRI/*.xml
%{_datadir}/ImageMagick-7/*.xml
%{_libdir}/libMagickCore-7.Q16HDRI.so.10
%{_libdir}/libMagickCore-7.Q16HDRI.so.10.*
%{_libdir}/libMagickWand-7.Q16HDRI.so.10
%{_libdir}/libMagickWand-7.Q16HDRI.so.10.*
%{_libdir}/libMagick++-7.Q16HDRI.so.5
%{_libdir}/libMagick++-7.Q16HDRI.so.5.*
%{_libdir}/ImageMagick-7.1.2/modules-Q16HDRI/*

%changelog
%autochangelog
