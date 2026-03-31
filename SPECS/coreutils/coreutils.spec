# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        GNU Core Utilities
Name:           coreutils
Version:        9.10
Release:        %autorelease
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/coreutils/
VCS:            git:https://github.com/coreutils/coreutils.git
#!RemoteAsset:  sha256:16535a9adf0b10037364e2d612aad3d9f4eca3a344949ced74d12faf4bd51d25
Source0:        https://ftpmirror.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  DEFAULT_POSIX2_VERSION=200112
BuildOption(conf):  --enable-no-install-program=kill

BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  texinfo
BuildRequires:  autoconf
BuildRequires:  automake

Provides:       /bin/rm

%description
These are the GNU core utilities.  This package is the union of
the GNU fileutils, sh-utils, and textutils packages.

  [ arch b2sum base32 base64 basename basenc cat chcon chgrp chmod chown chroot
  cksum comm cp csplit cut date dd df dir dircolors dirname du echo env expand
  expr factor false fmt fold groups head hostid id install join
  link ln logname ls md5sum mkdir mkfifo mknod mktemp mv nice nl nohup
  nproc numfmt od paste pathchk pinky pr printenv printf ptx pwd readlink
  realpath rm rmdir runcon seq sha1sum sha224sum sha256sum sha384sum sha512sum
  shred shuf sleep sort split stat stdbuf stty sum sync tac tail tee test
  timeout touch tr true truncate tsort tty uname unexpand uniq unlink
  uptime users vdir wc who whoami yes

%install -a
# TODO: Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%doc NEWS README THANKS
%{_bindir}/*
%{_libexecdir}/coreutils/libstdbuf.so
%{_mandir}/man1/*
%{_infodir}/coreutils.info*

%changelog
%{?autochangelog}
