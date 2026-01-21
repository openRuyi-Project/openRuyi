# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bison
Version:        3.8.2
Release:        %autorelease
Summary:        The GNU Parser Generator
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/bison/bison.html
VCS:            git:https://https.git.savannah.gnu.org/git/bison.git
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/bison/bison-%{version}.tar.xz
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/bison/bison-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildRequires:  flex
BuildRequires:  gcc-c++

Requires:       m4

%description
Bison is a parser generator similar to yacc(1).

%install -a
%find_lang bison-runtime --all-name --generate-subpackages

%files
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/AUTHORS
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/README
%exclude %{_docdir}/%{name}/THANKS
%exclude %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/examples
%dir %{_datadir}/aclocal
%{_bindir}/bison
%{_bindir}/yacc
%{_libdir}/liby.a
%{_datadir}/bison
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/bison-i18n.m4
%{_infodir}/bison.info*.gz
%{_mandir}/man1/bison.1%{?ext_man}
%{_mandir}/man1/yacc.1%{?ext_man}

%changelog
%{?autochangelog}
