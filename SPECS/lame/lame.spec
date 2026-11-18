# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lame
Version:        4.0
Release:        %autorelease
Summary:        Free MP3 audio compressor
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lame.sourceforge.net/
VCS:            svn:https://svn.code.sf.net/p/lame/svn/trunk/lame
#!RemoteAsset:  sha256:3df5124d5ad3a98312ffd7ba6a9b36230e4f8a3e66d3ce0f425e336c32d216eb
Source:         https://downloads.sourceforge.net/project/lame/lame/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# Upstream SVN r6562 (SF #524): split UTF-8 and UTF-16 ID3v2 tag paths and add
# id3tag_set_fieldvalue_utf8(); omits test/unit/* additions not shipped in 4.0 tarball.
# https://sourceforge.net/p/lame/svn/6562/
# https://sourceforge.net/p/lame/bugs/524/
Patch1000:      1000-fix-id3v2-utf8-tag-path.patch
# Upstream SVN r6564 (SF #515): export hip_set_pinfo and hip_finish_pinfo for
# dynamic frontend linking; omits doc/html/history.html 4.1 section hunk.
# https://sourceforge.net/p/lame/svn/6564/
# https://sourceforge.net/p/lame/bugs/515/
Patch1001:      1001-export-decoder-analysis-hooks.patch

BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-mp3rtp
%ifarch x86_64
BuildOption(conf):  --enable-nasm
%endif
BuildOption(conf):  LIBS="-ltinfo"

BuildRequires:  make
BuildRequires:  pkgconfig(libmpg123)
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
%{_libdir}/pkgconfig/lame.pc
%{_includedir}/lame/

%changelog
%autochangelog
