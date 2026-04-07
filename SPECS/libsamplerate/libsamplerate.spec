# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsamplerate
Version:        0.2.2
Release:        %autorelease
Summary:        Audio sample rate conversion library
License:        BSD-2-Clause
URL:            https://libsndfile.github.io/libsamplerate/
VCS:            git:https://github.com/libsndfile/libsamplerate.git
#!RemoteAsset:  sha256:3258da280511d24b49d6b08615bbe824d0cacc9842b0e4caf11c52cf2b043893
Source0:        https://github.com/libsndfile/libsamplerate/releases/download/%{version}/libsamplerate-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-sndfile
BuildOption(conf):  --disable-alsa
BuildOption(conf):  --disable-fftw

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

%description
libsamplerate is a high quality audio sample rate conversion library for
converting sampled audio data to a different sample rate.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains headers and pkg-config metadata for developing
applications against libsamplerate.

%files
%license COPYING
%doc ChangeLog NEWS README.md
%doc %{_pkgdocdir}/*
%{_libdir}/libsamplerate.so.*

%files devel
%{_includedir}/samplerate.h
%{_libdir}/libsamplerate.so
%{_libdir}/pkgconfig/samplerate.pc

%changelog
%autochangelog
