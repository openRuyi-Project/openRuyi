# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define package_version 9.2
%define patchlevel 0390

%define vimdir vim92

Name:           vim
Version:        %{package_version}.%{patchlevel}
Release:        %autorelease
Summary:        A popular VI editor derivative with enhanced functionality
License:        Vim AND LGPL-2.1-or-later AND MIT AND GPL-1.0-only AND (GPL-2.0-only OR Vim) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND OPUBL-1.0 AND Apache-2.0
URL:            https://www.vim.org/
VCS:            git:https://github.com/vim/vim
#!RemoteAsset:  sha256:18f5abda9cae11359cc9625370fc142bdfbefbbc4c07aad55d21dca5d5bdbdf2
Source0:        https://github.com/vim/vim/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gettext
BuildRequires:  pkgconfig(libacl)
BuildRequires:  libtool
BuildRequires:  pkgconfig(ncurses)

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package     -n xxd
Summary:        A hex dump utility

%description -n xxd
xxd creates a hex dump of a given file or standard input.  It can also convert
a hex dump back to its original binary form.

%install -a
# Remove unecessary duplicate manpages - 251
rm -rf %{buildroot}%{_mandir}/fr.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/fr.UTF-8/
rm -rf %{buildroot}%{_mandir}/pl.ISO8859-2/
rm -rf %{buildroot}%{_mandir}/pl.UTF-8/
rm -rf %{buildroot}%{_mandir}/ru.KOI8-R/
rm -rf %{buildroot}%{_mandir}/it.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/it.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.UTF-8/
rm -rf %{buildroot}%{_mandir}/de.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/de.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/tr.ISO8859-9/
rm -rf %{buildroot}%{_mandir}/tr.UTF-8/

%find_lang %{name} --all-name --with-man --generate-subpackages

# Nothing to check.
%check

%files
%license %{_datadir}/%{name}/%{vimdir}/LICENSE
%doc %{_datadir}/%{name}/%{vimdir}/README.txt
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/view
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/pack
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhelp.vim
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhighlight.vim
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/%{vimdir}/tools
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/view.*
%{_mandir}/man1/evim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
# If we need GUI then add these back
%exclude %{_datadir}/applications/vim.desktop
%exclude %{_datadir}/applications/gvim.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/gvim.*
%exclude %{_datadir}/icons/locolor/*/apps/gvim.*
# Language files
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(cs.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/cs.cp1250
%lang(da) %{_datadir}/%{name}/%{vimdir}/lang/da
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(hu) %{_datadir}/%{name}/%{vimdir}/lang/hu
%lang(hy) %{_datadir}/%{name}/%{vimdir}/lang/hy
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ja.euc-jp) %{_datadir}/%{name}/%{vimdir}/lang/ja.euc-jp
%lang(ja.sjis) %{_datadir}/%{name}/%{vimdir}/lang/ja.sjis
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(lv) %{_datadir}/%{name}/%{vimdir}/lang/lv
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(nl) %{_datadir}/%{name}/%{vimdir}/lang/nl
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pl.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/pl.UTF-8
%lang(pl.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/pl.cp1250
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(ru.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/ru.cp1251
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sk.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/sk.cp1250
%lang(sr) %{_datadir}/%{name}/%{vimdir}/lang/sr
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(ta) %{_datadir}/%{name}/%{vimdir}/lang/ta
%lang(tr) %{_datadir}/%{name}/%{vimdir}/lang/tr
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(uk.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/uk.cp1251
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_CN.cp936) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.cp936
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8

%files -n xxd
%license LICENSE
%{_bindir}/xxd
%{_mandir}/man1/xxd.*

%changelog
%autochangelog
