# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# perl modules are not installed in global path
%global __provides_exclude ^(libtool|perl)\\(

Name:           texinfo
Version:        7.2
Release:        %autorelease
Summary:        Tools needed to create Texinfo format documentation files
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/texinfo/texinfo.html
VCS:            git:https://https.git.savannah.gnu.org/git/texinfo.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

# Fix tests treat the extra stderr output as failures
Patch0:         0001-texinfo-7.2-fix-perl-precedence-warnings.patch

BuildRequires:  perl
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  help2man

Requires:       perl

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.

%package        devel
Summary:        Development files for Texinfo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for Texinfo

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/texinfo.tex doc/txi-*.tex doc/refcard/*.pdf
%license COPYING
%{_bindir}/makeinfo
%{_bindir}/texi2any
%{_bindir}/pod2texi
%{_bindir}/info
%{_bindir}/texindex
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%{_bindir}/pdftexi2dvi
%{_bindir}/install-info
%{_datadir}/texinfo
%{_datadir}/texi2any
%{_infodir}/texinfo*
%{_infodir}/texi2any_api.info*
%{_infodir}/texi2any_internals.info*
%{_infodir}/info-stnd.info*
%{_datadir}/locale/*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/texi2any.1*
%{_mandir}/man1/pod2texi.1*
%{_mandir}/man1/info.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man1/pdftexi2dvi.1*
%{_mandir}/man5/texinfo.5*
%{_mandir}/man5/info.5*

%files devel
%{_libdir}/texi2any/*

%changelog
%autochangelog
