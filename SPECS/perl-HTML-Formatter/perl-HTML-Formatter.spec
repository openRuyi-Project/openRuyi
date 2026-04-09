# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Formatter
Version:        2.16
Release:        %autorelease
Summary:        Base class for HTML formatters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Formatter
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NI/NIGELM/HTML-Formatter-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Font::Metrics::Courier)
BuildRequires:  perl(Font::Metrics::CourierBold)
BuildRequires:  perl(Font::Metrics::CourierBoldOblique)
BuildRequires:  perl(Font::Metrics::CourierOblique)
BuildRequires:  perl(Font::Metrics::Helvetica)
BuildRequires:  perl(Font::Metrics::HelveticaBold)
BuildRequires:  perl(Font::Metrics::HelveticaBoldOblique)
BuildRequires:  perl(Font::Metrics::HelveticaOblique)
BuildRequires:  perl(Font::Metrics::TimesBold)
BuildRequires:  perl(Font::Metrics::TimesBoldItalic)
BuildRequires:  perl(Font::Metrics::TimesItalic)
BuildRequires:  perl(Font::Metrics::TimesRoman)
BuildRequires:  perl(HTML::Element) >= 3.15
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(HTML::Element) >= 3.15

%description
HTML::Formatter is a base class for classes that take HTML and format it to
some output format. When you take an object of such a base class and call
$formatter-format( $tree )> with an HTML::TreeBuilder (or HTML::Element)
object, they return the appropriately formatted string for the input HTML.

%prep
%setup -q -n HTML-Formatter-%{version}

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
