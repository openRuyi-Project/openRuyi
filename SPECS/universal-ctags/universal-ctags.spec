# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           universal-ctags
Version:        6.2.0
Release:        %autorelease
Summary:        A program to generate language tag files
License:        GPL-2.0-only
URL:            https://github.com/universal-ctags/ctags
#!RemoteAsset
Source:         https://github.com/universal-ctags/ctags/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(yaml-0.1)
# for tests
BuildRequires:  python3

Requires(post):  update-alternatives
Requires(preun):  update-alternatives

%description
Universal ctags, a maintained fork from Darren Hieberts project, generates tag
files from source code for various languages to be used with Editors like
Emacs, Vim and several others.

%prep -a
echo '#define CTAGS_REPOINFO "%{version}"' > main/repoinfo.h

%conf -p
autoreconf -fiv

%install -a
install -D -m 755 ctags %{buildroot}%{_bindir}/universal-ctags

%post
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
update-alternatives --install  %{_bindir}/ctags ctags %{_bindir}/universal-ctags 25 \
  --slave %{_mandir}/man1/ctags.1.gz ctags.1 %{_mandir}/man1/universal-ctags.1.gz

%postun
if [ ! -f %{_bindir}/ctags ] ; then
   update-alternatives --remove ctags %{_bindir}/universal-ctags
fi

%files
%license COPYING
%{_bindir}/universal-ctags
%{_bindir}/ctags
%{_bindir}/optscript
%{_bindir}/readtags
%ghost %{_sysconfdir}/alternatives/ctags

%changelog
%autochangelog
