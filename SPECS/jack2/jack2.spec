# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Prevent client connection crashes with LTO: https://github.com/jackaudio/jack2/issues/485
%global _lto_cflags %{nil}

Name:           jack2
Version:        1.9.22
Release:        %autorelease
Summary:        The Jack Audio Connection Kit
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/jackaudio/jack2
#!RemoteAsset:  sha256:1e42b9fc4ad7db7befd414d45ab2f8a159c0b30fcd6eee452be662298766a849
Source0:        https://github.com/jackaudio/jack2/archive/refs/tags/v%{version}.tar.gz

# Support Python 3.12+; adapted from https://gitlab.com/ita1024/waf/-/commit/d2060dfd8af4edb5824153ff24e207b39ecd67a2
Patch0:         0001-remove-imp.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(opus)
BuildRequires:  doxygen

BuildSystem:    waf
BuildOption(conf):  --mandir=%{_mandir}/man1
BuildOption(conf):  --htmldir=%{_docdir}/%{name}/reference/html
BuildOption(conf):  --doxygen
BuildOption(conf):  --dbus
BuildOption(conf):  --classic
BuildOption(conf):  --alsa
BuildOption(conf):  --samplerate=yes
BuildOption(conf):  --opus=yes

Requires:       python3dist(dbus-python)

%description
JACK is a low-latency audio server, written primarily for the Linux operating
system. It can connect a number of different applications to an audio device, as
well as allowing them to share audio between themselves. Its clients can run in
their own processes (i.e. as a normal application), or can they can run within a
JACK server (i.e. a "plugin").

%package        devel
Summary:        Header files for Jack
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files for the Jack Audio Connection Kit.

%check
# Upstream has no automated Waf test target.

%files
%doc ChangeLog.rst README.rst README_NETJACK2
%license COPYING
%{_bindir}/jackd
%{_libdir}/jack/
%{_libdir}/libjack.so.*
%{_libdir}/libjacknet.so.*
%{_libdir}/libjackserver.so.*
%{_mandir}/man1/jackd*.1*
%{_bindir}/jackdbus
%{_datadir}/dbus-1/services/org.jackaudio.service
%{_bindir}/jack_control

%files devel
%{_docdir}/%{name}/reference/html/
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjacknet.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%changelog
%autochangelog
