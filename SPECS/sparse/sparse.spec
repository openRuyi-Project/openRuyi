# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sparse
Version:        0.6.4
Release:        %autorelease
Summary:        A semantic parser for C source files
License:        MIT
URL:            https://sparse.wiki.kernel.org/
VCS:            git:https://git.kernel.org/pub/scm/devel/sparse/sparse.git
#!RemoteAsset
Source:         https://www.kernel.org/pub/software/devel/sparse/dist/sparse-%{version}.tar.xz
BuildSystem:    autotools

# https://git.kernel.org/pub/scm/devel/sparse/sparse.git/commit/?id=adceff0ab6e3d8bf43de52e2c2fbebf27db30deb
Patch1:         0001-linearize.c-fix-buffer-overrun-warning-from-fortify.patch


BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  HAVE_LLVM=no
BuildOption(build):  HAVE_GTK=no
BuildOption(install):  PREFIX="%{_prefix}"
BuildOption(install):  BINDIR="%{_bindir}"
BuildOption(install):  LIBDIR="%{_libdir}"
BuildOption(install):  INCLUDEDIR="%{_includedir}"
BuildOption(install):  PKGCONFIGDIR="%{_libdir}/pkgconfig"
BuildOption(install):  HAVE_LLVM=no
BuildOption(install):  HAVE_GTK=no
BuildOption(check):  HAVE_LLVM=no
BuildOption(check):  HAVE_GTK=no

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)

%description
Sparse is a semantic parser of C source files, primarily used in the
development and debugging of the Linux kernel. It creates a semantic parse
tree for further analysis.

# No configure.
%conf

%files
%license LICENSE
%doc README FAQ
%{_bindir}/sparse
%{_bindir}/semind
%{_bindir}/cgcc
%{_bindir}/c2xml
%{_mandir}/man1/*

%changelog
%autochangelog
