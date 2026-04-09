# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libheif
Version:        1.21.2
Release:        %autorelease
Summary:        HEIF and AVIF file format decoder and encoder
License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/strukturag/libheif
#!RemoteAsset:  sha256:79996de959d28ca82ef070c382304683f5cdaf04cbe2953a74587160a3710a36
Source0:        https://github.com/strukturag/libheif/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# no av1 support,so skip the tests.
Patch0:         0001-libheif-no-av1-tests.patch

BuildOption(conf):  -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF
BuildOption(conf):  -DPLUGIN_DIRECTORY=%{_libdir}/libheif
BuildOption(conf):  -DWITH_DAV1D=ON
BuildOption(conf):  -DWITH_DAV1D_PLUGIN=OFF
BuildOption(conf):  -DWITH_JPEG_DECODER=ON
BuildOption(conf):  -DWITH_JPEG_ENCODER=ON
BuildOption(conf):  -DWITH_OpenJPEG_DECODER=ON
BuildOption(conf):  -DWITH_OpenJPEG_DECODER_PLUGIN=OFF
BuildOption(conf):  -DWITH_OpenJPEG_ENCODER=ON
BuildOption(conf):  -DWITH_OpenJPEG_ENCODER_PLUGIN=OFF
BuildOption(conf):  -DWITH_OPENJPH_DECODER=ON
BuildOption(conf):  -DWITH_OPENJPH_ENCODER=ON
BuildOption(conf):  -DWITH_OPENJPH_ENCODER_PLUGIN=OFF
BuildOption(conf):  -DWITH_OpenH264_DECODER=ON
BuildOption(conf):  -DWITH_OpenH264_ENCODER=ON
BuildOption(conf):  -DWITH_UNCOMPRESSED_CODEC=ON
BuildOption(conf):  -DWITH_GDK_PIXBUF=ON
BuildOption(conf):  -DWITH_EXAMPLE_HEIF_VIEW=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(sdl2)

%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format)
file format decoder and encoder.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
rm -rf third-party/

%files
%license COPYING
%doc README.md
%{_libdir}/libheif.so.*
%dir %{_libdir}/libheif
%{_bindir}/heif-*
%{_mandir}/man1/heif-*
%{_datadir}/thumbnailers/heif.thumbnailer

%files devel
%{_includedir}/libheif/
%{_libdir}/cmake/libheif/
%{_libdir}/pkgconfig/libheif.pc
%{_libdir}/libheif.so

%changelog
%autochangelog
