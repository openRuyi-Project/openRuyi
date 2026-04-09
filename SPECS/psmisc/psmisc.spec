# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           psmisc
Version:        23.7
Release:        %autorelease
Summary:        Utilities for managing processes on your system
License:        GPL-2.0-or-later
URL:            https://gitlab.com/psmisc/psmisc
#!RemoteAsset
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --enable-selinux
BuildOption(conf):  --disable-rpath

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(ncurses)

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall, fuser and pslog.  The pstree command displays
a tree structure of all of the running processes on your system.  The
killall command sends a specified signal (SIGTERM if nothing is specified)
to processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems. The pslog
command shows the path of log files owned by a given process.

%conf -p
# We need to generate po/POTFILES.in
# Otherwise build will fail
grep -h src/ po/*.po|\
 sed -r 's/^#: //'|\
 tr ' ' '\n'|\
 sort -t : -k1,1 -u|\
 sed -r 's/:[0-9]+$//' > po/POTFILES.in
echo %version > .tarball-version
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/fuser
%{_bindir}/killall
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_bindir}/prtstat
%{_bindir}/pslog
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pslog.1*
%ifarch x86_64
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1*
%else
%exclude %{_mandir}/man1/peekfd.1*
%endif

%changelog
%autochangelog
