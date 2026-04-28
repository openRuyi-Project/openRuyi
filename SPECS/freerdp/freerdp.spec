# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond ffmpeg 1
%bcond sdl_client 0
%bcond webview 0

Name:           freerdp
Version:        3.22.0
Release:        %autorelease
Summary:        Free implementation of the Remote Desktop Protocol (RDP)
License:        Apache-2.0
URL:            http://www.freerdp.com/
VCS:            git:https://github.com/FreeRDP/FreeRDP
#!RemoteAsset:  sha256:f4af346eb12b5558f7a93e585e55f523a5cbbb53e6e3a0bf3ffed8f293e2a5b8
Source0:        https://github.com/FreeRDP/FreeRDP/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=ON
BuildOption(conf):  -DWITH_MANPAGES=ON
BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DWITH_CHANNELS=ON
BuildOption(conf):  -DWITH_CLIENT=ON
BuildOption(conf):  -DWITH_FUSE=ON
BuildOption(conf):  -DWITH_GSM=OFF
BuildOption(conf):  -DWITH_LAME=OFF
BuildOption(conf):  -DWITH_JPEG=ON
BuildOption(conf):  -DWITH_JSONC_REQUIRED=ON
BuildOption(conf):  -DWITH_ZLIB=ON
BuildOption(conf):  -DWITH_SERVER=ON
BuildOption(conf):  -DWITH_SHADOW_X11=ON
%if %{with ffmpeg}
BuildOption(conf):  -DWITH_FFMPEG=ON
BuildOption(conf):  -DWITH_DSP_FFMPEG=ON
BuildOption(conf):  -DWITH_VIDEO_FFMPEG=ON
BuildOption(conf):  -DWITH_SWSCALE=ON
%else
BuildOption(conf):  -DWITH_FFMPEG=OFF
BuildOption(conf):  -DWITH_DSP_FFMPEG=OFF
BuildOption(conf):  -DWITH_VIDEO_FFMPEG=OFF
BuildOption(conf):  -DWITH_SWSCALE=OFF
%endif
BuildOption(conf):  -DWITH_X11=ON
BuildOption(conf):  -DWITH_XCURSOR=ON
BuildOption(conf):  -DWITH_XEXT=ON
BuildOption(conf):  -DWITH_XKBFILE=ON
BuildOption(conf):  -DWITH_XI=ON
BuildOption(conf):  -DWITH_XINERAMA=ON
BuildOption(conf):  -DWITH_XRENDER=ON
BuildOption(conf):  -DWITH_XV=ON
BuildOption(conf):  -DWITH_WAYLAND=ON
BuildOption(conf):  -DWITH_ALSA=ON
BuildOption(conf):  -DWITH_PULSE=ON
BuildOption(conf):  -DWITH_OPENSSL=ON
BuildOption(conf):  -DWITH_CUPS=ON
BuildOption(conf):  -DWITH_KRB5=ON
%if %{with sdl_client}
BuildOption(conf):  -DWITH_CLIENT_SDL=ON
%else
BuildOption(conf):  -DWITH_CLIENT_SDL=OFF
%endif
%if %{with webview}
BuildOption(conf):  -DWITH_WEBVIEW=ON
%else
BuildOption(conf):  -DWITH_WEBVIEW=OFF
%endif
BuildOption(conf):  -DWITH_OPENCL=OFF
BuildOption(conf):  -DWITH_OPENH264=OFF
BuildOption(conf):  -DWITH_SOXR=ON
BuildOption(conf):  -DWITH_IPP=OFF
BuildOption(conf):  -DWITH_PCSC=OFF
BuildOption(conf):  -DWITH_PKCS11=OFF

BuildRequires:  cmake >= 3.13
BuildRequires:  pkgconfig(soxr)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake(json-c)
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif

Provides:       xfreerdp

%description
FreeRDP is a free implementation of the Remote Desktop Protocol (RDP).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for FreeRDP.

%package        server
Summary:        Server support for %{name}

%description    server
Server support for FreeRDP.

%install -a
find %{buildroot} -name "*.a" -delete

%files
%license LICENSE
%doc README.md ChangeLog
%{_bindir}/winpr-hash
%{_bindir}/winpr-makecert
%{_bindir}/xfreerdp
%{_bindir}/sfreerdp
%{_bindir}/sfreerdp-server
%{_mandir}/man1/winpr-hash.1*
%{_mandir}/man1/winpr-makecert.1*
%{_mandir}/man1/xfreerdp.1*
%{_bindir}/wlfreerdp
%{_mandir}/man1/wlfreerdp.1*
%{_datadir}/FreeRDP/
%{_libdir}/freerdp3/
%{_libdir}/libfreerdp-client3.so.*
%{_libdir}/libfreerdp3.so.*
%{_libdir}/libuwac0.so.*
%{_libdir}/librdtk0.so.*
%{_libdir}/libfreerdp-server3.so.*
%{_libdir}/libfreerdp-server-proxy3.so.*
%{_libdir}/libfreerdp-shadow3.so.*
%{_libdir}/libfreerdp-shadow-subsystem3.so.*
%{_libdir}/libwinpr3.so.*
%{_libdir}/libwinpr-tools3.so.*
%{_mandir}/man7/wlog.*

%files devel
%{_includedir}/freerdp3/
%{_includedir}/uwac0/
%{_includedir}/rdtk0/
%{_libdir}/cmake/FreeRDP3/
%{_libdir}/cmake/FreeRDP-Client3/
%{_libdir}/cmake/uwac0/
%{_libdir}/cmake/rdtk0/
%{_libdir}/libfreerdp-client3.so
%{_libdir}/libfreerdp3.so
%{_libdir}/libuwac0.so
%{_libdir}/librdtk0.so
%{_libdir}/pkgconfig/freerdp3.pc
%{_libdir}/pkgconfig/freerdp-client3.pc
%{_libdir}/pkgconfig/uwac0.pc
%{_libdir}/pkgconfig/rdtk0.pc
%{_libdir}/cmake/FreeRDP-Proxy3/
%{_libdir}/cmake/FreeRDP-Server3/
%{_libdir}/cmake/FreeRDP-Shadow3/
%{_libdir}/pkgconfig/freerdp-server-proxy3.pc
%{_libdir}/pkgconfig/freerdp-server3.pc
%{_libdir}/pkgconfig/freerdp-shadow3.pc
%{_libdir}/libfreerdp-server*.so
%{_libdir}/libfreerdp-shadow*.so
%{_libdir}/cmake/WinPR3/
%{_libdir}/cmake/WinPR-tools3/
%{_includedir}/winpr3/
%{_libdir}/libwinpr3.so
%{_libdir}/libwinpr-tools3.so
%{_libdir}/pkgconfig/winpr3.pc
%{_libdir}/pkgconfig/winpr-tools3.pc

%files server
%{_bindir}/freerdp-proxy
%{_bindir}/freerdp-shadow-cli
%{_mandir}/man1/freerdp-proxy.1*
%{_mandir}/man1/freerdp-shadow-cli.1*

%changelog
%{?autochangelog}
