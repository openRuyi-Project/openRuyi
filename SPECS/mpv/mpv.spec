# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mpv
Version:        0.41.0
Release:        %autorelease
Summary:        Movie player playing most video formats and DVDs
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            https://github.com/mpv-player/mpv
#!RemoteAsset:  sha256:ee21092a5ee427353392360929dc64645c54479aefdb5babc5cfbb5fad626209
Source0:        https://github.com/mpv-player/mpv/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  --auto-features=disabled
BuildOption(conf):  -Dcplayer=true
BuildOption(conf):  -Dlibmpv=true
BuildOption(conf):  -Dwerror=false
BuildOption(conf):  -Dbuild-date=false
BuildOption(conf):  -Diconv=enabled
BuildOption(conf):  -Djpeg=enabled
BuildOption(conf):  -Dlibavdevice=enabled
BuildOption(conf):  -Dzlib=enabled
BuildOption(conf):  -Dwayland=enabled
BuildOption(conf):  -Ddmabuf-wayland=enabled
BuildOption(conf):  -Degl=enabled
BuildOption(conf):  -Degl-x11=enabled
BuildOption(conf):  -Degl-wayland=enabled
BuildOption(conf):  -Degl-drm=enabled
BuildOption(conf):  -Dgbm=enabled
BuildOption(conf):  -Ddrm=enabled
BuildOption(conf):  -Dsdl2-audio=enabled
BuildOption(conf):  -Dsdl2-gamepad=enabled
BuildOption(conf):  -Dsdl2-video=enabled
BuildOption(conf):  -Dvaapi=enabled
BuildOption(conf):  -Dvaapi-x11=enabled
BuildOption(conf):  -Dvaapi-wayland=enabled
BuildOption(conf):  -Dvaapi-drm=enabled
BuildOption(conf):  -Dvdpau=enabled
BuildOption(conf):  -Dvdpau-gl-x11=enabled
BuildOption(conf):  -Dalsa=enabled
BuildOption(conf):  -Dpulse=enabled
BuildOption(conf):  -Dpipewire=enabled
BuildOption(conf):  -Djack=enabled
BuildOption(conf):  -Dopenal=enabled
BuildOption(conf):  -Dvapoursynth=enabled
BuildOption(conf):  -Ddvdnav=enabled
BuildOption(conf):  -Dlibbluray=enabled
BuildOption(conf):  -Dlibarchive=enabled
BuildOption(conf):  -Dlcms2=enabled
BuildOption(conf):  -Dzimg=enabled
BuildOption(conf):  -Dx11=enabled
BuildOption(conf):  -Dgl-x11=enabled
BuildOption(conf):  -Dplain-gl=enabled
# need [5.1-5.3),but we have 5.4
BuildOption(conf):  -Dlua=disabled
BuildOption(conf):  -Dmanpage-build=disabled
BuildOption(conf):  -Dhtml-build=disabled
BuildOption(conf):  -Dcaca=enabled
BuildOption(conf):  -Dcuda-hwaccel=enabled
BuildOption(conf):  -Dcuda-interop=enabled
BuildOption(conf):  -Dvulkan=disabled
BuildOption(conf):  -Djavascript=enabled
BuildOption(conf):  -Drubberband=enabled
BuildOption(conf):  -Duchardet=enabled

BuildRequires:  meson
BuildRequires:  libatomic
BuildRequires:  pkgconfig(libplacebo)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.57
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  bash-completion
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(uchardet)

%description
Mpv is a movie player based on MPlayer and mplayer2.

%package        devel
Summary:        Development package for libmpv
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development header files and libraries for Mpv.

%files
%license LICENSE.GPL LICENSE.LGPL Copyright
%{_bindir}/mpv
%{_docdir}/mpv/
%{_datadir}/applications/mpv.desktop
%{_datadir}/icons/hicolor/*/apps/mpv*.*
%{bash_completions_dir}/mpv
%{_datadir}/zsh/site-functions/_mpv
%{_datadir}/fish/vendor_completions.d/mpv.fish
%{_datadir}/metainfo/mpv.metainfo.xml
%{_libdir}/libmpv.so.2*

%files devel
%{_includedir}/mpv/
%{_libdir}/libmpv.so
%{_libdir}/pkgconfig/mpv.pc

%changelog
%autochangelog
