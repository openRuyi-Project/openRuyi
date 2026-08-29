# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-WrapI18N
Version:        0.06
Release:        %autorelease
Summary:        Line wrapping module with support for multibyte, fullwidth, and combining characters and languages without whitespaces between words
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-WrapI18N
#!RemoteAsset:  sha256:4bd29a17f0c2c792d12c1005b3c276f2ab0fae39c00859ae1741d7941846a488
Source0:        https://www.cpan.org/authors/id/K/KU/KUBOTA/Text-WrapI18N-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Text::CharWidth) >= 0.02

%description
This module intends to be a better Text::Wrap module. This module is needed
to support multibyte character encodings such as UTF-8, EUC-JP, EUC-KR,
GB2312, and Big5. This module also supports characters with irregular
widths, such as combining characters (which occupy zero columns on
terminal, like diacritical marks in UTF-8) and fullwidth characters (which
occupy two columns on terminal, like most of east Asian characters). Also,
minimal handling of languages which doesn't use whitespaces between words
(like Chinese and Japanese) is supported.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
