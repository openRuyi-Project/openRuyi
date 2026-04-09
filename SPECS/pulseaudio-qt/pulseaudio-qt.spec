# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pulseaudio-qt
Summary:        Qt bindings for PulseAudio
Version:        1.8.1
Release:        %autorelease
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://invent.kde.org/libraries/pulseaudio-qt
#!RemoteAsset:  sha256:79619c55b94808aa7d307fb234ad39a1096d088f21f806be0e788be79a76b3c9
Source:         https://download.kde.org/stable/pulseaudio-qt/pulseaudio-qt-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package        qt6-devel
Summary:        Development files for %{name} (Qt6)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt6-devel
%{summary}.

%files
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.*

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_includedir}/pulseaudioqt_version.h
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc

%changelog
%autochangelog
