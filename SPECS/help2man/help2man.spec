# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           help2man
Version:        1.49.3
Release:        %autorelease
Summary:        Script for generating man pages from --help output
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/help2man/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --enable-nls

BuildRequires:  perl-Locale-gettext
BuildRequires:  perl

Requires:       perl-Locale-gettext
Requires:       perl

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a way
to generate a placeholder man page pointing to that resource while
still providing some useful information.

%install -a
%find_lang %{name} --with-man --generate-subpackages

# No check
%check

%files
%license COPYING
%doc NEWS README THANKS debian/changelog
%{_bindir}/help2man
%{_libdir}/help2man/
%{_infodir}/help2man.info%{?ext_info}
%{_mandir}/man1/help2man.1%{?ext_man}
%license COPYING
%{_infodir}/help2man-*.info%{?ext_info}
%dir %{_mandir}/??
%dir %{_mandir}/??/man1

%changelog
%autochangelog
