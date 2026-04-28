# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rubberband
Version:        4.0.0
Release:        %autorelease
Summary:        Audio time-stretching and pitch-shifting library
License:        GPL-2.0-or-later
URL:            https://www.breakfastquay.com/rubberband/
VCS:            git:https://hg.sr.ht/~breakfastquay/rubberband
#!RemoteAsset:  sha256:af050313ee63bc18b35b2e064e5dce05b276aaf6d1aa2b8a82ced1fe2f8028e9
Source:         https://breakfastquay.com/files/releases/rubberband-%{version}.tar.bz2
BuildSystem:    meson

BuildOption(conf):  -Dladspa=disabled
BuildOption(conf):  -Dlv2=disabled
BuildOption(conf):  -Dvamp=disabled
BuildOption(conf):  -Djni=disabled
BuildOption(conf):  -Dfft=fftw
BuildOption(conf):  -Dresampler=libsamplerate

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  boost-devel

%description
Rubber Band Library is a high quality software library for audio time-stretching and pitch-shifting.
It permits you to change the tempo and pitch of an audio stream or recording dynamically and independently of one another.

%package        libs
Summary:        Audio time-stretching and pitch-shifting library

%description    libs
Rubber Band is an audio time-stretching and pitch-shifting library.
This package provides a shared library for use by applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Rubber Band is an audio time-stretching and pitch-shifting library.
The %{name}-devel package contains libraries and header files for developing applications.

%install -a
rm -rf %{buildroot}%{_libdir}/*.a

%files
%license COPYING
%doc README.md
%{_bindir}/rubberband
%{_bindir}/rubberband-r3

%files libs
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc CHANGELOG
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc

%changelog
%autochangelog
