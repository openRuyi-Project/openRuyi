# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           portaudio
Version:        19.7.0
Release:        %autorelease
Summary:        Portable cross-platform Audio I/O library
License:        MIT
URL:            https://www.portaudio.com
VCS:            git:https://github.com/PortAudio/portaudio.git
#!RemoteAsset:  sha256:5af29ba58bbdbb7bbcefaaecc77ec8fc413f0db6f4c4e286c40c3e1b83174fa0
Source0:        https://github.com/PortAudio/portaudio/archive/v%{version}.tar.gz#/portaudio-%{version}.tar.gz
BuildSystem:    cmake

# Backport upstream CMake install-dir and shared-library versioning fixes from
# master, including PortAudio/portaudio@99b4ee829ce171bc52a4eb9f026ea6168147af43.
Patch0:         0001-backport-cmake-install-libdir-and-soname.patch

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DPA_BUILD_STATIC=OFF
BuildOption(conf):  -DPA_BUILD_TESTS=OFF
BuildOption(conf):  -DPA_BUILD_EXAMPLES=OFF

BuildRequires:  cmake

%description
PortAudio is a free, cross-platform, open-source audio I/O library.
It provides a single API for recording and playing sound across
Linux (ALSA, JACK, OSS), macOS (CoreAudio), and Windows (WASAPI, ASIO, WDM-KS).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and development libraries for building applications
that use PortAudio.

%files
%doc %{_docdir}/portaudio/README.md
%license LICENSE.txt
%license %{_docdir}/portaudio/LICENSE.txt
%{_libdir}/libportaudio.so.*

%files devel
%{_includedir}/portaudio.h
%{_libdir}/libportaudio.so
%{_libdir}/pkgconfig/portaudio-2.0.pc
%{_libdir}/cmake/portaudio/

%changelog
%autochangelog
