# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# disable parallel build,as there is some bug.
# https://github.com/festvox/flite/pull/92#issuecomment-1481980430
%global _smp_mflags -j1

Name:           flite
Version:        2.2
Release:        %autorelease
Summary:        Small, fast speech synthesis engine (text-to-speech)
License:        MIT
URL:            https://github.com/festvox/flite
#!RemoteAsset
Source0:        https://github.com/festvox/flite/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --with-audio=pulseaudio

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ed
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  texinfo

%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine.

%package        devel
Summary:        Development files for flite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for Flite.

%conf -p
autoreconf -fiv

%install -a
rm %{buildroot}%{_libdir}/libflite*.a

%check
# No tests here.

%files
%license COPYING
%doc ACKNOWLEDGEMENTS README.md
%{_libdir}/libflite*.so.*
%{_bindir}/flite*

%files devel
%{_libdir}/libflite*.so
%{_includedir}/flite/

%changelog
%autochangelog
