# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode-Locale
Version:        1.05
Release:        %autorelease
Summary:        Determine the locale encoding
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Encode-Locale
#!RemoteAsset:  sha256:176fa02771f542a4efb1dbc2a4c928e8f4391bf4078473bd6040d8f11adb0ec1
Source0:        https://www.cpan.org/authors/id/G/GA/GAAS/Encode-Locale-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Encode) >= 2
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(Test::More)

Requires:       perl(Encode) >= 2

%description
In many applications it's wise to let Perl use Unicode for the strings it
processes. Most of the interfaces Perl has to the outside world are still
byte based. Programs therefore need to decode byte strings that enter the
program from the outside and encode them again on the way out.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
