# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           emacs
Version:        30.2
Release:        %autorelease
Summary:        The extensible, customizable, self-documenting real-time display editor
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/emacs
VCS:            git:https://git.savannah.gnu.org/git/emacs.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/emacs/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/emacs/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):  --without-x
BuildOption(conf):  --with-pgtk

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  gzip
BuildRequires:  bzip2
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)

Requires(post): update-alternatives
Requires(postun): update-alternatives


%description
GNU Emacs is a powerful, customizable, self-documenting, modeless text
editor. It contains special code editing features, a scripting language
(elisp), and the capability to read mail, news, and more without leaving
the editor.

%conf -p
autoreconf -fiv

# No tests
%check

%install -a
mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/gctags
if [ -e %{buildroot}%{_bindir}/etags ]; then
  mv %{buildroot}%{_bindir}/etags %{buildroot}%{_bindir}/etags.emacs
else
  ln -s gctags %{buildroot}%{_bindir}/etags.emacs
fi

mv %{buildroot}%{_mandir}/man1/ctags.1%{?ext_man} %{buildroot}%{_mandir}/man1/gctags.1%{?ext_man}
if [ -e %{buildroot}%{_mandir}/man1/etags.1%{?ext_man} ]; then
  mv %{buildroot}%{_mandir}/man1/etags.1%{?ext_man} %{buildroot}%{_mandir}/man1/etags.emacs.1%{?ext_man}
else
  ln -s gctags.1%{?ext_man} %{buildroot}%{_mandir}/man1/etags.emacs.1%{?ext_man}
fi

%post
%{_sbindir}/update-alternatives --install %{_bindir}/ctags ctags %{_bindir}/gctags 15 \
  --slave %{_mandir}/man1/ctags.1%{?ext_man} ctags.1%{?ext_man} %{_mandir}/man1/gctags.1%{?ext_man}

%postun
if [ "$1" -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove ctags %{_bindir}/gctags
fi

%files
%license COPYING
%{_bindir}/emacs
%{_bindir}/emacsclient
%{_bindir}/ebrowse
%{_bindir}/etags.emacs
%{_bindir}/gctags
%{_bindir}/emacs-%{version}
%{_includedir}/emacs-module.h
%{_mandir}/man1/emacs.1*
%{_mandir}/man1/emacsclient.1*
%{_mandir}/man1/ebrowse.1*
%{_mandir}/man1/etags.emacs.1*
%{_mandir}/man1/gctags.1*
%dir %{_datadir}/emacs/%{version}
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/site-lisp
%{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%{version}/lisp
%dir %{_libexecdir}/emacs/%{version}
%{_libexecdir}/emacs/%{version}/%{_host}/movemail
%{_libexecdir}/emacs/%{version}/%{_host}/hexl
%{_libexecdir}/emacs/%{version}/%{_host}/rcs2log
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document23.svg
%{_datadir}/icons/hicolor/*/apps/emacs.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/apps/emacs.ico
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_datadir}/glib-2.0/schemas/org.gnu.emacs.defaults.gschema.xml
%{_datadir}/metainfo/emacs.metainfo.xml
%{_infodir}/*
%{_libexecdir}/emacs/%{version}/%{_host}/emacs-*.pdmp
%{_libdir}/systemd/user/emacs.service

%changelog
%autochangelog
