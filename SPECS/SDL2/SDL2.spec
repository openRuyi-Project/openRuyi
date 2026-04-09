# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond static 1

Name:           SDL2
Version:        2.32.10
Release:        %autorelease
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/libsdl-org/SDL
#!RemoteAsset
Source:         https://github.com/libsdl-org/SDL/archive/refs/tags/release-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSDL_DLOPEN=ON
BuildOption(conf):  -DSDL_VIDEO_KMSDRM=OFF
BuildOption(conf):  -DSDL_ARTS=OFF
BuildOption(conf):  -DSDL_ESD=OFF
BuildOption(conf):  -DSDL_NAS=OFF
BuildOption(conf):  -DSDL_PULSEAUDIO=OFF
BuildOption(conf):  -DSDL_PULSEAUDIO_SHARED=ON
BuildOption(conf):  -DSDL_JACK=OFF
BuildOption(conf):  -DSDL_JACK_SHARED=ON
BuildOption(conf):  -DSDL_PIPEWIRE=OFF
BuildOption(conf):  -DSDL_PIPEWIRE_SHARED=ON
BuildOption(conf):  -DSDL_ALSA=ON
BuildOption(conf):  -DSDL_VIDEO_WAYLAND=OFF
BuildOption(conf):  -DSDL_LIBDECOR_SHARED=ON
BuildOption(conf):  -DSDL_VIDEO_VULKAN=OFF
BuildOption(conf):  -DSDL_SSE3=OFF
BuildOption(conf):  -DSDL_RPATH=OFF
BuildOption(conf):  -DSDL_UNIX_CONSOLE_BUILD=ON
%if %{with static}
BuildOption(conf):  -DSDL_STATIC=ON
BuildOption(conf):  -DSDL_STATIC_PIC=ON
%else
BuildOption(conf):  -DSDL_STATIC=OFF
%endif

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

%package        devel
Summary:        Development files for SDL2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the libraries, include files, and other resources needed for
developing SDL applications.

%if %{with static}
%package        static
Summary:        Static libraries for SDL2
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static libraries for SDL2.
%endif

%prep -a
sed -i -e 's/\r//g' TODO.txt README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.txt README-SDL.txt

%install -a

%files
%license LICENSE.txt
%doc BUGS.txt CREDITS.txt README-SDL.txt
%{_libdir}/libSDL2-2.0.so.0*

%files devel
%doc README.md TODO.txt WhatsNew.txt
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/libSDL2main.a
%{_libdir}/pkgconfig/sdl2.pc
%{_libdir}/cmake/SDL2/
%{_includedir}/SDL2/
%{_datadir}/aclocal/*
%{_libdir}/libSDL2_test.a

%if %{with static}
%files static
%license LICENSE.txt
%{_libdir}/libSDL2.a
%endif

%changelog
%autochangelog
