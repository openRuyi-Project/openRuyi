# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-B-Keywords
Version:        1.29
Release:        %autorelease
Summary:        Lists of reserved barewords and symbol names
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/B-Keywords
#!RemoteAsset:  sha256:e0aa19d3390409f0ece7342ab041c5b432c31d7cf1abf182c134b6aab78784b0
Source0:        https://www.cpan.org/authors/id/R/RU/RURBAN/B-Keywords-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(B)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
B::Keywords supplies several arrays of exportable keywords: @Scalars,
  @Arrays, @Hashes, @Filehandles, @Symbols, @Functions, @Barewords,
  @BarewordsExtra, @TieIOMethods, @UNIVERSALMethods and @ExporterSymbols.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
