# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ntfs-3g
Version:        2022.10.3
Release:        %autorelease
Summary:        NTFS userspace driver for Linux
License:        GPL-2.0-or-later
URL:            https://github.com/tuxera/ntfs-3g
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#%{name}-%{version}.tar.gz
BuildSystem:    autotools

# I originally don't want to fix this but here we are - 251
Patch2000:      2000-Fix-sbindir.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-ldconfig
BuildOption(conf):  --enable-posix-acls
BuildOption(conf):  --enable-extras
BuildOption(conf):  --enable-crypto
BuildOption(conf):  --enable-quarantined
BuildOption(conf):  --exec-prefix=/
BuildOption(conf):  --with-fuse=external

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hwinfo)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(uuid)

%description
NTFS-3G is a stable, open source, GPL licensed, POSIX, read/write NTFS
driver for Linux and many other operating systems. It allows for
read/write access to NTFS partitions which can be shared with Windows XP,
Windows Server 2003, Windows 2000, Windows Vista, Windows 7, Windows 8/8.1,
Windows 10, and Windows 11.

%package        devel
Summary:        Development files and libraries for ntfs-3g
Requires:       %{name}{?_isa} = %{version}-%{release}

%description    devel
Headers and libraries for developing applications that use ntfs-3g
functionality.

%conf -p
autoreconf -fiv

%install -a
ln -s -f %{_sbindir}/mount.ntfs-3g %{buildroot}%{_sbindir}/mount.ntfs

%files
%doc AUTHORS ChangeLog CREDITS NEWS README
%license COPYING
%{_sbindir}/mount.ntfs
%{_sbindir}/mount.ntfs-3g
%{_sbindir}/mount.lowntfs-3g
%{_sbindir}/mkfs.ntfs
%{_sbindir}/mkntfs
%{_sbindir}/ntfsclone
%{_sbindir}/ntfscp
%{_sbindir}/ntfslabel
%{_sbindir}/ntfsresize
%{_sbindir}/ntfsundelete
%{_bindir}/ntfs-3g
%{_bindir}/ntfs-3g.probe
%{_bindir}/lowntfs-3g
# Tools
%{_bindir}/ntfscat
%{_bindir}/ntfscluster
%{_bindir}/ntfscmp
%{_bindir}/ntfsfix
%{_bindir}/ntfsinfo
%{_bindir}/ntfsls
%{_bindir}/ntfssecaudit
%{_bindir}/ntfsusermap
# Extras
%{_bindir}/ntfsck
%{_bindir}/ntfsdecrypt
%{_bindir}/ntfsdump_logfile
%{_bindir}/ntfsfallocate
%{_bindir}/ntfsmftalloc
%{_bindir}/ntfsmove
%{_bindir}/ntfsrecover
%{_bindir}/ntfstruncate
%{_bindir}/ntfswipe
%{_libdir}/libntfs-3g.so.*
%{_mandir}/man8/mount.lowntfs-3g.*
%{_mandir}/man8/mount.ntfs-3g.*
%{_mandir}/man8/ntfs-3g*
%{_mandir}/man8/mkntfs.8*
%{_mandir}/man8/mkfs.ntfs.8*
%{_mandir}/man8/ntfs[^m][^o]*.8*

%files devel
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so
%{_libdir}/pkgconfig/libntfs-3g.pc

%changelog
%autochangelog
