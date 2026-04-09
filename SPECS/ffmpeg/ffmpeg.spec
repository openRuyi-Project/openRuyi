# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# For a complete build enable this
%bcond all_codecs 0
%bcond vmaf 1

# Enable NVIDIA NVENC/NVDEC hardware acceleration support via ffnvcodec
%bcond ffnvcodec 0

%bcond lv2 0

%if %{with all_codecs}
%bcond rtmp 1
%bcond vvc 1
%bcond x264 1
%bcond x265 1
%else
%bcond rtmp 0
%bcond vvc 0
%bcond x264 0
%bcond x265 0
%endif

Name:           ffmpeg
Version:        8.0.1
Release:        %autorelease
Summary:        A complete solution to record, convert and stream audio and video
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
VCS:            git:https://git.ffmpeg.org/ffmpeg.git
#!RemoteAsset
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:        enable_decoders
Source2:        enable_encoders
BuildSystem:    autotools

# Fixes for reduced codec selection on free build
Patch1:         0001-ffmpeg-codec-choice.patch
# Allow to build with fdk-aac-free
# See https://bugzilla.redhat.com/show_bug.cgi?id=1501522#c112
Patch2:         0002-ffmpeg-allow-fdk-aac-free.patch
# Support building with EVC base profile libraries
Patch3:         0003-ffmpeg-support-evc-base-libraries.patch
# Add first_dts getter to libavformat for Chromium
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2240127
# Reference: https://crbug.com/1306560
Patch4:         0004-ffmpeg-chromium.patch

BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  gcc
BuildRequires:  lame-devel
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  libklvanc-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  make
%ifarch x86_64
BuildRequires:  nasm
%endif
BuildRequires:  pkgconfig(srt)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  perl(Pod::Man)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(libpulse)
%if %{with ffnvcodec}
BuildRequires:  pkgconfig(ffnvcodec)
%endif
%if %{with lv2}
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(oapv)
%endif
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(lc3)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vidstab)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
# BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  texinfo
%if %{with rtmp}
BuildRequires:  librtmp-devel
%endif
BuildRequires:  pkgconfig(xevdb)
BuildRequires:  pkgconfig(xeveb)
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif
%if %{with vmaf}
BuildRequires:  pkgconfig(libvmaf)
%endif

%description
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

%if %{without all_codecs}
This build of ffmpeg is limited in the number of codecs supported.
%endif

Summary:        A complete solution to record, convert and stream audio and video

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

%conf
cp %{SOURCE1} .
cp %{SOURCE2} .

# This is not a normal configure script, don't use %%configure
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --docdir=%{_docdir}/%{name} \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-ldflags="%{build_ldflags}" \
    --disable-htmlpages \
    --disable-static \
    --disable-stripping \
    --enable-pic \
    --enable-shared \
    --enable-gpl \
    --enable-version3 \
    --disable-amf \
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-alsa \
    --enable-bzlib \
    --disable-chromaprint \
    --disable-cuda-nvcc \
%if %{with ffnvcodec}
    --enable-cuvid \
%endif
    --enable-lcms2 \
    --enable-liblc3 \
%if %{with librtmp}
    --enable-librtmp \
%endif
    --enable-lto \
%if %{with vmaf}
    --enable-libvmaf \
%endif
%if %{with x264}
    --enable-libx264 \
%endif
%if %{with x265}
    --enable-libx265 \
%endif
%if %{with ffnvcodec}
    --enable-nvdec \
    --enable-nvenc \
%endif
    --disable-decklink \
    --disable-frei0r \
    --enable-gcrypt \
    --disable-gmp \
    --enable-gnutls \
    --enable-gray \
    --disable-iconv \
    --disable-ladspa \
    --disable-libaom \
    --disable-libaribb24 \
    --disable-libaribcaption \
    --enable-libass \
    --disable-libbluray \
    --disable-libbs2b \
    --disable-libcaca \
    --disable-libcdio \
    --disable-libcodec2 \
    --enable-libdav1d \
    --disable-libdavs2 \
    --enable-libdvdnav \
    --enable-libdvdread \
    --enable-libfdk-aac \
    --enable-libfontconfig \
    --enable-libfreetype \
    --enable-libfribidi \
    --disable-libgme \
    --enable-libharfbuzz \
    --disable-libgsm \
    --disable-libilbc \
    --disable-libjack \
    --disable-libjxl \
    --enable-libklvanc \
    --disable-liblensfun \
    --disable-liblcevc-dec \
    --disable-libmodplug \
    --enable-libmp3lame \
    --disable-libmysofa \
    --disable-libnpp \
    --disable-libopencore-amrnb \
    --disable-libopencore-amrwb \
    --disable-libopencv \
    --disable-liboapv \
    --disable-libopenh264 \
    --enable-libopenjpeg \
    --disable-libopenmpt \
    --disable-libopus \
    --enable-libpulse \
    --disable-libqrencode \
    --disable-libquirc \
    --disable-librabbitmq \
    --disable-librav1e \
    --disable-librist \
    --disable-librsvg \
    --disable-librubberband \
    --disable-libshaderc \
    --disable-libshine \
    --disable-libsmbclient \
    --enable-libsnappy \
    --disable-libsvtav1 \
    --enable-libsoxr \
    --disable-libspeex \
    --enable-libsrt \
    --enable-libssh \
    --disable-libtensorflow \
    --disable-libtesseract \
    --disable-libtheora \
    --disable-libtorch \
    --disable-libuavs3d \
    --enable-libtwolame \
    --disable-libv4l2 \
    --enable-libvidstab \
    --disable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --disable-libxavs2 \
    --disable-libxavs \
    --enable-libxcb \
    --enable-libxcb-shape \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxevdb \
    --enable-libxeveb \
    --enable-libxml2 \
    --disable-libxvid \
    --enable-libzimg \
    --disable-libzmq \
    --disable-libzvbi \
    --disable-lv2 \
    --enable-lzma \
    --enable-manpages \
    --disable-openal \
    --disable-openssl \
    --enable-pthreads \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --disable-v4l2-m2m \
    --disable-vaapi \
    --disable-vapoursynth \
    --enable-vdpau \
    --disable-vulkan \
    --disable-xlib \
    --enable-zlib \
%if %{without all_codecs}
    --enable-muxers \
    --enable-demuxers \
    --disable-hwaccels \
    --disable-encoders \
    --disable-decoders \
    --disable-decoder="h264,hevc,vc1,vvc" \
    --enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <enable_encoders)" \
    --enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <enable_decoders)" \
%endif

# Paranoia check
%if %{without all_codecs}
# DECODER
for i in H264 HEVC HEVC_RKMPP VC1 VVC; do
    grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done

# ENCODER
for i in LIBX264 LIBX264RGB LIBX265; do
    grep -q "#define CONFIG_${i}_ENCODER 0" config_components.h
done
for i in H264 HEVC; do
    for j in MF VIDEOTOOLBOX; do
        grep -q "#define CONFIG_${i}_${j}_ENCODER 0" config_components.h
    done
done
%endif

%build -a
make documentation
make alltools

# TODO: fix tests,here just skip it.
%check

%files
%doc CREDITS README.md
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_mandir}/man1/ff*.1*
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/ffprobe.xsd
%{_datadir}/ffmpeg/*.ffpreset
%{_libdir}/libavcodec.so.*
%{_libdir}/libavfilter.so.*
%{_libdir}/libavformat.so.*
%{_libdir}/libavdevice.so.*
%{_libdir}/libavutil.so.*
%{_libdir}/libswresample.so.*
%{_libdir}/libswscale.so.*

%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_datadir}/ffmpeg/examples
%{_includedir}/ffmpeg/libavcodec
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/libavcodec.so
%{_mandir}/man3/libavcodec.3*
%{_includedir}/ffmpeg/libavdevice
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/libavdevice.so
%{_mandir}/man3/libavdevice.3*
%{_includedir}/ffmpeg/libavfilter
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/libavfilter.so
%{_mandir}/man3/libavfilter.3*
%{_includedir}/ffmpeg/libavformat
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/libavformat.so
%{_mandir}/man3/libavformat.3*
%{_includedir}/ffmpeg/libavutil
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/libavutil.so
%{_mandir}/man3/libavutil.3*
%{_includedir}/ffmpeg/libswresample
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/libswresample.so
%{_mandir}/man3/libswresample.3*
%{_includedir}/ffmpeg/libswscale
%{_libdir}/pkgconfig/libswscale.pc
%{_libdir}/libswscale.so
%{_mandir}/man3/libswscale.3*

%changelog
%autochangelog
