# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsamplerate
Version:        0.2.2
Release:        %autorelease
Summary:        An audio Sample Rate Conversion library
License:        BSD-2-Clause
URL:            https://libsndfile.github.io/libsamplerate/
VCS:            git:https://github.com/libsndfile/libsamplerate
#!RemoteAsset:  sha256:3258da280511d24b49d6b08615bbe824d0cacc9842b0e4caf11c52cf2b043893
Source:         https://github.com/libsndfile/libsamplerate/releases/download/%{version}/libsamplerate-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3) >= 0.15.0
BuildRequires:  pkgconfig(sndfile) >= 1.0.6

%description
libsamplerate (also known as Secret Rabbit Code) is a library for performing sample rate conversion of audio data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/libsamplerate.so.0*

%files devel
%{_includedir}/samplerate.h
%{_libdir}/libsamplerate.so
%{_libdir}/pkgconfig/samplerate.pc
%{_pkgdocdir}/*

%changelog
%autochangelog
