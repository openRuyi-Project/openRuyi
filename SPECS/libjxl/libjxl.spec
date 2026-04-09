# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libjxl
Version:        0.11.2
Release:        %autorelease
Summary:        JPEG XL image format reference implementation
License:        BSD-3-Clause
URL:            https://github.com/libjxl/libjxl
#!RemoteAsset:  sha256:ab38928f7f6248e2a98cc184956021acb927b16a0dee71b4d260dc040a4320ea
Source0:        https://github.com/libjxl/libjxl/archive/v%{version}/libjxl-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DJPEGXL_FORCE_SYSTEM_HWY=ON
BuildOption(conf):  -DJPEGXL_FORCE_SYSTEM_BROTLI=ON
BuildOption(conf):  -DJPEGXL_FORCE_SYSTEM_LCMS2=ON
BuildOption(conf):  -DENABLE_CCACHE=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_PLUGINS=ON
BuildOption(conf):  -DJPEGXL_ENABLE_SKCMS=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_SJPEG=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_DOXYGEN=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_JPEGLI=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_BENCHMARK=OFF
BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DJPEGXL_ENABLE_DEVTOOLS=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(libhwy)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libwebp)

%description
This package contains a reference implementation of JPEG XL (encoder and
decoder).

%package        devel
Summary:        Development files for JPEG-XL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
JPEG XL is a raster-graphics file format that supports both lossy and
lossless compression.

%files
%license LICENSE
%doc CONTRIBUTING.md CONTRIBUTORS README.md
%{_bindir}/cjxl
%{_bindir}/djxl
%{_bindir}/jxlinfo
%{_bindir}/djxl_fuzzer_corpus
%{_bindir}/butteraugli_main
%{_bindir}/decode_and_encode
%{_bindir}/display_to_hlg
%{_bindir}/exr_to_pq
%{_bindir}/icc_simplify
%{_bindir}/pq_to_hlg
%{_bindir}/render_hlg
%{_bindir}/tone_map
%{_bindir}/texture_to_cube
%{_bindir}/generate_lut_template
%{_bindir}/ssimulacra_main
%{_bindir}/ssimulacra2
%{_bindir}/xyb_range
%{_bindir}/jxl_from_tree
%{_bindir}/local_tone_map
%{_libdir}/libjxl.so.*
%{_libdir}/libjxl_threads.so.*
%{_libdir}/libjxl_cms.so.*
%{_datadir}/mime/packages/image-jxl.xml

%files devel
%doc CONTRIBUTING.md
%{_includedir}/jxl/
%{_libdir}/libjxl.so
%{_libdir}/libjxl_threads.so
%{_libdir}/libjxl_cms.so
%{_libdir}/libjxl_extras_codec.a
%{_libdir}/pkgconfig/libjxl.pc
%{_libdir}/pkgconfig/libjxl_threads.pc
%{_libdir}/pkgconfig/libjxl_cms.pc

%changelog
%autochangelog
