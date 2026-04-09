# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           recutils
Version:        1.9
Release:        %autorelease
Summary:        A set of tools to access GNU recfile databases
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/recutils/
VCS:            git:https://https.git.savannah.gnu.org/git/recutils.git
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/recutils/recutils-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-recutils-1.9-mdbtools-0.9.patch
Patch1:         0002-recutils-c99.patch

BuildOption(conf):  CFLAGS="%{optflags} -Wno-error=implicit-function-declaration -Wno-error=incompatible-pointer-types"
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --without-mdb
BuildOption(conf):  --without-emacs

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(check)

%description
Recutils is a set of tools and libraries to access human-editable,
text-based databases called recfiles.

%package        devel
Summary:        Libraries and header files for recutils
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files for developing
applications that use the recutils library.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/recutils
%{_infodir}/*.info*

%files devel
%{_includedir}/rec.h
%{_libdir}/*.so

%changelog
%autochangelog
