# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-CSV
Version:        2.06
Release:        %autorelease
Summary:        Comma-separated values manipulator (using XS or PurePerl)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-CSV
#!RemoteAsset:  sha256:dfcaec925a788b0ba41e51bc6d16e21b0e98b4c7af9b79395090add75f5e506f
Source0:        https://www.cpan.org/authors/id/I/IS/ISHIGAKI/Text-CSV-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Text::CSV_XS) >= 1.60

Requires:       perl(Test::More) >= 0.92
Requires:       perl(Text::CSV_XS) >= 1.60

%description
Text::CSV is a thin wrapper for Text::CSV_XS-compatible modules now. All
the backend modules provide facilities for the composition and
decomposition of comma-separated values. Text::CSV uses Text::CSV_XS by
default, and when Text::CSV_XS is not available, falls back on
Text::CSV_PP, which is bundled in the same distribution as this module.

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
