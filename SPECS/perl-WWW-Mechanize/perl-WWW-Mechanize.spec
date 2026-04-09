# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-WWW-Mechanize
Version:        2.19
Release:        %autorelease
Summary:        Handy web browsing in a Perl object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-Mechanize
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Form) >= 6.08
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder) >= 5
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Request) >= 1.30
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Taint) >= 1.08
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(warnings)

Requires:       perl(HTML::Form) >= 6.08
Requires:       perl(HTML::TreeBuilder) >= 5
Requires:       perl(HTTP::Request) >= 1.30
Requires:       perl(Scalar::Util) >= 1.14

%description
WWW::Mechanize, or Mech for short, is a Perl module for stateful
programmatic web browsing, used for automating interaction with websites.

%prep
%setup -q -n WWW-Mechanize-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTORS perlcriticrc perlimports.toml perltidyrc README.md tidyall.ini

%changelog
%autochangelog
