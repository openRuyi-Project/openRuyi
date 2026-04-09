# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-B-Keywords
Version:        1.28
Release:        %autorelease
Summary:        Lists of reserved barewords and symbol names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/B-Keywords
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RU/RURBAN/B-Keywords-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(B)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
B::Keywords supplies several arrays of exportable keywords: @Scalars,
  @Arrays, @Hashes, @Filehandles, @Symbols, @Functions, @Barewords,
  @BarewordsExtra, @TieIOMethods, @UNIVERSALMethods and @ExporterSymbols.

%prep
%setup -q -n B-Keywords-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
