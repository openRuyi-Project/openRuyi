# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lame
Version:        3.100
Release:        %autorelease
Summary:        Free MP3 audio compressor
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lame.sourceforge.net/
VCS:            svn:https://svn.code.sf.net/p/lame/svn/trunk/lame
#!RemoteAsset
Source:         https://downloads.sourceforge.net/lame/lame-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-mp3rtp
%ifarch x86_64
BuildOption(conf):  --enable-nasm
%endif
BuildOption(conf):  LIBS="-ltinfo"

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
%ifarch x86_64
BuildRequires:  nasm
%endif

%description
LAME is an open source MP3 encoder whose quality and speed matches
commercial encoders. LAME handles MPEG-1, 2 and 2.5 layer III encoding
with both constant and variable bitrates.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package development files for %{name}.

%install -a
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc README TODO USAGE doc/html/*.html
%{_bindir}/lame
%{_bindir}/mp3rtp
%{_mandir}/man1/lame.1*
%doc ChangeLog
%license COPYING LICENSE
%{_libdir}/libmp3lame.so.0*

%files devel
%doc API HACKING STYLEGUIDE
%{_libdir}/libmp3lame.so
%{_includedir}/lame/


%changelog
%autochangelog
