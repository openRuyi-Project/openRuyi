# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# VLC 3.0.x still uses the autotools configure/make flow.
# The upstream Qt interface can be built against Qt6 in openRuyi, so keep the
# GUI enabled by default while deferring the optional interfaces that still need
# extra packaging work.
%bcond qt 1
%bcond lua 1
%bcond live555 0
%bcond upnp 0
%bcond notify 1
%bcond wayland 0

Name:           vlc
Version:        3.0.23
Release:        %autorelease
Summary:        Multimedia player and streaming framework
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.videolan.org/vlc/
VCS:            git:https://code.videolan.org/videolan/vlc.git
#!RemoteAsset:  sha256:e891cae6aa3ccda69bf94173d5105cbc55c7a7d9b1d21b9b21666e69eff3e7e0
Source0:        https://get.videolan.org/vlc/%{version}/vlc-%{version}.tar.xz
BuildSystem:    autotools

# skins2 depends on the Qt interface and is therefore deferred together with
# the Qt5 stack question.
BuildOption(conf):  --disable-skins2
# These codec backends are not packaged in-tree yet.
BuildOption(conf):  --disable-a52
BuildOption(conf):  --disable-faad
BuildOption(conf):  --disable-mad
# chromaprint support needs extra multimedia stack work and is not required for
# a functional first package.
BuildOption(conf):  --disable-chromaprint
# chromecast support needs protobuf-lite handling that has not been validated
# in openRuyi packaging yet.
BuildOption(conf):  --disable-chromecast
# JACK is intentionally deferred until the preferred jack provider strategy in
# openRuyi is settled.
BuildOption(conf):  --disable-jack
# libplacebo is not packaged in-tree yet.
BuildOption(conf):  --disable-libplacebo
BuildOption(conf):  --enable-libgcrypt
BuildOption(conf):  --enable-libva
BuildOption(conf):  --enable-vdpau
BuildOption(conf):  --enable-avcodec
BuildOption(conf):  --enable-avformat
BuildOption(conf):  --enable-swscale
BuildOption(conf):  --enable-alsa
BuildOption(conf):  --enable-pulse
BuildOption(conf):  --enable-dbus
BuildOption(conf):  --enable-dvdread
BuildOption(conf):  --enable-dvdnav
BuildOption(conf):  --enable-samplerate
BuildOption(conf):  --enable-taglib
BuildOption(conf):  --enable-gnutls
BuildOption(conf):  --enable-xcb
BuildOption(conf):  --enable-xvideo
# Upstream builds helper generators with a native C compiler during configure.
BuildOption(conf):  BUILDCC=gcc
%if %{with qt}
BuildOption(conf):  --enable-qt
%else
BuildOption(conf):  --disable-qt
%endif
%if %{with lua}
BuildOption(conf):  --enable-lua
%else
BuildOption(conf):  --disable-lua
%endif
%if %{with live555}
BuildOption(conf):  --enable-live555
%else
BuildOption(conf):  --disable-live555
%endif
%if %{with upnp}
BuildOption(conf):  --enable-upnp
%else
BuildOption(conf):  --disable-upnp
%endif
%if %{with notify}
BuildOption(conf):  --enable-notify
%else
BuildOption(conf):  --disable-notify
%endif
%if %{with wayland}
BuildOption(conf):  --enable-wayland
%else
# Upstream marks Wayland support as incomplete and it also needs wayland-scanner
# provider validation in openRuyi before we make it a hard requirement.
BuildOption(conf):  --disable-wayland
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xproto)
%if %{with qt}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
# Qt6 has no standalone QtX11Extras module; X11 integration is in QtGui.
%endif
%if %{with live555}
BuildRequires:  pkgconfig(live555)
%endif
%if %{with lua}
BuildRequires:  pkgconfig(lua)
%endif
%if %{with upnp}
BuildRequires:  pkgconfig(libupnp)
%endif
%if %{with notify}
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
%endif
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
%endif

%description
VLC is a libre multimedia player and streaming framework capable of playing
local files, optical media and network streams through libvlc and a large
collection of loadable plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers, pkg-config metadata and linker symlinks for
developing applications against libvlc and libvlccore.

%package        doc
Summary:        Additional documentation for %{name}

%description    doc
This package contains upstream examples, Lua integration notes and additional
reference documentation for VLC and libvlc.

%post
# Refresh the plugin cache on install/upgrade so VLC does not keep using a
# stale plugins.dat generated at build time.
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins >/dev/null 2>&1 || :

%postun
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/vlc/plugins/plugins.dat || :
fi

%install -a
# Drop an internal static archive that is not meant to be shipped.
rm -f %{buildroot}%{_libdir}/vlc/libcompat.a

# TODO: Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%check
# TODO: re-enable checks after validating the Qt6-enabled build in CI/OBS.
# The upstream check suite runs check_POTFILES.sh and expects generated Qt UI
# headers from the configured interface set.
:

%files -f %{name}.lang
%license COPYING COPYING.LIB
%{_bindir}/cvlc
%{_bindir}/qvlc
%{_bindir}/rvlc
%{_bindir}/vlc
%{_bindir}/vlc-wrapper
%{_datadir}/applications/*vlc*.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/kde4/apps/solid/actions/*vlc*.desktop
%{_datadir}/metainfo/*vlc*.xml
%{_datadir}/vlc/
# Runtime libraries
%{_libdir}/libvlc.so.*
%{_libdir}/libvlccore.so.*
%{_libdir}/vlc/
%{_mandir}/man1/*vlc*.1*

%files devel
%{_includedir}/vlc/
%{_libdir}/libvlc.so
%{_libdir}/libvlccore.so
%{_libdir}/pkgconfig/libvlc.pc
%{_libdir}/pkgconfig/vlc-plugin.pc

%files doc
%doc AUTHORS NEWS THANKS
%doc %{_pkgdocdir}/*

%changelog
%autochangelog
