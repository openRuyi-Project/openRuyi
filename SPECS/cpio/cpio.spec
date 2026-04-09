# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cpio
Version:        2.15
Release:        %autorelease
Summary:        A Backup and Archiving Utility
License:        GPL-3.0-only
URL:            https://www.gnu.org/software/cpio/cpio.html
VCS:            git:https://git.savannah.gnu.org/git/cpio.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
BuildSystem:    autotools

# GCC15: give xstat a real prototype
Patch0:         0001-fix-xstat-prototype.patch

BuildOption(conf):  --with-rmt="%{_bindir}/rmt"
BuildOption(conf):  --enable-mt
BuildOption(conf):  --program-transform-name='s/^mt$/gnumt/'

BuildRequires:  autoconf
BuildRequires:  automake

Suggests:       rmt
Suggests:       %{name}-mt = %{version}-%{release}

%description
GNU cpio is a program to manage archives of files. Cpio copies files
into or out of a cpio or tar archive. An archive is a file that contains
other files plus information about them, such as their pathname, owner,
time stamps, and access permissions. The archive can be another file on
the disk, a magnetic tape, or a pipe.

%package        mt
Summary:        Tape drive control utility
Requires:       %{name} = %{version}-%{release}
Requires(post): update-alternatives
Provides:       mt
Conflicts:      mt

%description mt
This package includes the 'mt', a local tape drive control program.

%conf -p
autoreconf -fiv

%build -p
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -fcommon -std=gnu11"

%install -a
%find_lang %{name} --generate-subpackages

%post mt
if [ ! -f %{_bindir}/gnumt ] ; then
   "%{_sbindir}/update-alternatives" --remove mt %{_bindir}/gnumt
fi

%files
%license COPYING
%doc NEWS ChangeLog
%{_bindir}/cpio
%{_infodir}/cpio.info*
%{_mandir}/man1/cpio.1*

%files mt
%ghost %{_bindir}/mt
%{_bindir}/gnumt
%ghost %{_mandir}/man1/mt.1*
%{_mandir}/man1/gnumt.1*

%changelog
%autochangelog
