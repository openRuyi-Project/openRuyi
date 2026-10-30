# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           partclone
Version:        0.3.52
Release:        %autorelease
Summary:        File system aware partition imaging tool
# Partclone's own code is GPL-2.0-or-later. The bundled btrfs, xfs and f2fs
# libraries and the helper programs add more licenses:
#   btrfs: GPL-2.0-only, GPL-2.0-or-later, GPL-2.0-only WITH Linux-syscall-note,
#          GPL-2.0-only OR MIT, BSD-2-Clause, BSD-3-Clause,
#          CC0-1.0 OR OpenSSL OR Apache-2.0, LGPL-2.1-or-later
#   xfs: GPL-2.0-only, LGPL-2.1-only
#   f2fs: GPL-2.0-only
#   ntfsfixboot: GPL-3.0-or-later
#   gettext.h: LGPL-2.0-or-later
License:        BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR OpenSSL OR Apache-2.0) AND GPL-2.0-only AND (GPL-2.0-only OR MIT) AND (GPL-2.0-only WITH Linux-syscall-note) AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:            https://partclone.org/
VCS:            git:https://github.com/Thomas-Tsai/partclone.git
#!RemoteAsset:  sha256:15fcfafb42fea1fdbc9a022b2dc8cc49f60d49fee969b41ef3d05d944471dc12
Source:         https://github.com/Thomas-Tsai/partclone/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-apfs
BuildOption(conf):  --enable-btrfs
BuildOption(conf):  --enable-exfat
BuildOption(conf):  --enable-extfs
BuildOption(conf):  --enable-f2fs
BuildOption(conf):  --enable-fat
BuildOption(conf):  --enable-hfsp
BuildOption(conf):  --enable-minix
BuildOption(conf):  --enable-ncursesw
BuildOption(conf):  --enable-ntfs
BuildOption(conf):  --enable-xfs
BuildOption(conf):  --enable-zfs
BuildOption(build):  MAN_STYLESHEET=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
BuildOption(install):  MAN_STYLESHEET=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(com_err)
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libntfs-3g)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
Partclone provides utilities to back up and restore the used blocks of a
partition. Unlike a raw disk image, only the blocks in use are copied,
which keeps images small. Existing file system libraries are used to read
and write the file system, so the image is compatible with the original
file system after a restore.

Supported file systems include ext2/3/4, XFS, Btrfs, ZFS, NTFS,
FAT12/16/32, exFAT, F2FS, HFS+, APFS and Minix.

%conf -p
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/partclone.*
%{_datadir}/bash-completion/completions/partclone
%{_mandir}/man8/partclone.*

%changelog
%autochangelog
