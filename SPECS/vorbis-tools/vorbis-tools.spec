# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vorbis-tools
Version:        1.4.3
Release:        %autorelease
Summary:        Ogg Vorbis Tools
License:        GPL-2.0-only
URL:            https://www.xiph.org/
VCS:            git:https://gitlab.xiph.org/xiph/vorbis-tools.git
#!RemoteAsset
Source0:        https://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  gettext-tools
#BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(speex)
BuildRequires:  chrpath

Provides:       vorbis = %{version}-%{release}

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free, general-purpose
compressed audio format for mid to high quality (8kHz-48.0kHz, 16+ bit, polyphonic) audio
and music at fixed and variable bitrates from 16 to 128 kbps/channel. This places Vorbis
in the same competitive class as audio representations such as MPEG-4 (AAC), and similar
to, but higher performance than MPEG-1/2 audio layer 3, MPEG-4 audio (TwinVQ), WMA and PAC.

%conf -p
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=format-security"

%install -a
rm -rf %{buildroot}%{_docdir}

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README CHANGES ogg123/ogg123rc-example
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
